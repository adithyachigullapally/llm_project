import os
import sys
import sqlite3
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver

# --- SETUP PATHS ---
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from schema import ConversationState, Message
from tools.car_tools import execute_tool
from agents.personas import GLOBAL_EXPERT_PROMPT 

load_dotenv(override=True)
client = OpenAI()

# ==========================================
# NODE 1: THE ROUTER (UPDATED)
# ==========================================
def router_node(state: ConversationState):
    """
    Decides if we need Local, Web, Chat, OR 'COMPARE' (Parallel).
    """
    last_msg = state.messages[-1].content
    print(f"\n🚦 [ROUTER] Analyzing: '{last_msg}'")
    
    # We ask GPT to classify. If comparison, we ask it to split the query.
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.0, 
        messages=[
            {"role": "system", "content": """
             Classify the user intent.
             
             1. If asking for stock/inventory -> Output: LOCAL
             2. If asking for general price/info -> Output: WEB
             3. If casual chat -> Output: CHAT
             4. If asking to COMPARE two cars (e.g. "BMW vs Audi") -> Output: COMPARE|Car1 Name|Car2 Name
                (Example: "COMPARE|BMW X5|Audi Q7")
             """},
            {"role": "user", "content": last_msg}
        ]
    )
    
    decision_raw = response.choices[0].message.content.strip()
    
    # Parse the decision
    if "COMPARE" in decision_raw:
        # Format is "COMPARE|Car A|Car B"
        parts = decision_raw.split("|")
        return {
            "tool_used": "COMPARE",
            "parallel_query_1": parts[1] if len(parts) > 1 else "Car 1",
            "parallel_query_2": parts[2] if len(parts) > 2 else "Car 2"
        }
    else:
        # Standard Single Path
        return {"tool_used": decision_raw.upper()}

# ==========================================
# NODE 2: LOCAL SPECIALIST
# ==========================================
def local_specialist_node(state: ConversationState):
    print("   └── 🏢 [LOCAL AGENT] Checking Showroom Inventory...")
    last_msg = state.messages[-1].content
    result = execute_tool("search_inventory", {"query": last_msg})
    return {"messages": [Message(role="assistant", content=result)]}

# ==========================================
# NODE 3: GLOBAL RESEARCHER (Standard)
# ==========================================
def global_researcher_node(state: ConversationState):
    print("   └── 🌍 [WEB AGENT] Searching Internet...")
    last_msg = state.messages[-1].content
    result = execute_tool("web_search_cars", {"query": last_msg})
    return {"messages": [Message(role="assistant", content=result)]}

# ==========================================
# 🆕 NODE 3.1 & 3.2: PARALLEL RESEARCHERS
# ==========================================
def research_worker_1(state: ConversationState):
    # Searches for Car 1
    query = state.parallel_query_1
    print(f"   └── 🏎️  [WORKER 1] Searching for '{query}'...")
    result = execute_tool("web_search_cars", {"query": query})
    return {"messages": [Message(role="assistant", content=f"SPECS FOR {query}: {result}")]}

def research_worker_2(state: ConversationState):
    # Searches for Car 2
    query = state.parallel_query_2
    print(f"   └── 🚙 [WORKER 2] Searching for '{query}'...")
    result = execute_tool("web_search_cars", {"query": query})
    return {"messages": [Message(role="assistant", content=f"SPECS FOR {query}: {result}")]}

# ==========================================
# NODE 4: J.A.R.V.I.S
# ==========================================
def voice_synthesizer_node(state: ConversationState):
    """
    Acts as the 'Voice'. Cleans text for audio so it sounds natural.
    """
    # Grab context (works for both single and parallel paths)
    recent_context = "\n".join([m.content for m in state.messages[-3:]])
    
    print(f"   └── 🗣️  [JARVIS] Synthesizing Natural Audio...")

    system_instruction = (
        GLOBAL_EXPERT_PROMPT + 
        "\n\nTASK: Rewrite the data above into smooth SPOKEN text. No headers. No 'Verdict' titles."
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Data Found: {recent_context}"}
        ]
    )

    final_text = response.choices[0].message.content

    # 🛡️ SAFETY SCRUBBER: Remove "robotic" formatting
    # This removes bolding, headers, and common AI titles
    clean_text = final_text.replace("**", "").replace("###", "").replace("##", "")
    clean_text = clean_text.replace("Verdict:", "").replace("Conclusion:", "").replace("Comparison:", "")
    
    return {"messages": [Message(role="assistant", content=clean_text)]}

# ==========================================
# LOGIC & GRAPH DEFINITION
# ==========================================
def route_logic(state: ConversationState):
    decision = state.tool_used
    
    if "COMPARE" in decision:
        return ["worker_1", "worker_2"] # <--- 🚀 RETURNS A LIST (PARALLEL)
    elif "LOCAL" in decision: 
        return "local"
    elif "WEB" in decision: 
        return "web"
    else: 
        return "synthesizer"

def get_multi_agent_app():
    workflow = StateGraph(ConversationState)
    
    # Add Nodes
    workflow.add_node("router", router_node)
    workflow.add_node("local_specialist", local_specialist_node)
    workflow.add_node("global_researcher", global_researcher_node)
    
    # 🆕 Add Parallel Nodes
    workflow.add_node("worker_1", research_worker_1)
    workflow.add_node("worker_2", research_worker_2)
    
    workflow.add_node("JARVIS", voice_synthesizer_node)
    
    # Entry Point
    workflow.set_entry_point("router")
    
    # Conditional Routing
    workflow.add_conditional_edges(
        "router",
        route_logic,
        {
            "local": "local_specialist", 
            "web": "global_researcher", 
            "worker_1": "worker_1", # Path A
            "worker_2": "worker_2", # Path B
            "synthesizer": "JARVIS" 
        }
    )
    
    # Standard Edges (All roads lead to JARVIS)
    workflow.add_edge("local_specialist", "JARVIS")
    workflow.add_edge("global_researcher", "JARVIS")
    workflow.add_edge("worker_1", "JARVIS") # Merge point
    workflow.add_edge("worker_2", "JARVIS") # Merge point
    workflow.add_edge("JARVIS", END)
    
    # Memory
    memory_folder = os.path.join(root_dir, "memory")
    if not os.path.exists(memory_folder):
        os.makedirs(memory_folder)
    
    db_path = os.path.join(memory_folder, "agent_history.db")
    conn = sqlite3.connect(db_path, check_same_thread=False)
    memory = SqliteSaver(conn)
    
    return workflow.compile(checkpointer=memory)