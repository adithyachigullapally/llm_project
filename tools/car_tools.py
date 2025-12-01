import os
import sys
from pathlib import Path
from dotenv import load_dotenv 

# --- 1. FORCE LOAD .ENV ---
# We load this immediately so all keys are available to the whole app
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

# Add root to path so we can import schema
sys.path.append(str(Path(__file__).parent.parent))

from typing import Dict, Any, List
from tavily import TavilyClient
from data.car_database import search_inventory

# --- 2. CHECK ALL API KEYS ---
tavily_api_key = os.getenv("TAVILY_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

print("\n" + "="*40)
print("🔑  API KEY STATUS CHECK")
print("="*40)

# Check Tavily
if tavily_api_key:
    print(f"✅ Tavily Search    : FOUND ({tavily_api_key[:5]}...)")
else:
    print("❌ Tavily Search    : MISSING (Web search will fail)")

# Check OpenAI
if openai_api_key:
    print(f"✅ OpenAI LLM       : FOUND ({openai_api_key[:5]}...)")
else:
    print("❌ OpenAI LLM       : MISSING (Brain will fail)")

# Check LangChain (Optional)
if langchain_api_key:
    print(f"✅ LangChain Tracing: FOUND ({langchain_api_key[:5]}...)")
else:
    print("⚠️ LangChain Tracing: NOT FOUND (App works, but no logs)")
print("="*40 + "\n")

# Initialize Tavily Client
tavily = TavilyClient(api_key=tavily_api_key) if tavily_api_key else None

def web_search_cars_tool(query: str) -> str:
    """
    Searches the global web for car recommendations, prices, and specs.
    """
    if not tavily:
        return "⚠️ Error: Web search is not enabled (missing TAVILY_API_KEY)."
    
    print(f"   (Tavily: Searching for '{query}'...)")
    
    try:
        response = tavily.search(
            query=query, 
            search_depth="advanced",
            max_results=5,
            include_domains=[
                "caranddriver.com", "topgear.com", "edmunds.com", 
                "autocarindia.com", "zigwheels.com", "mbusa.com", "ferrari.com",
                "bikewale.com"
            ]
        )
        
        results_text = "Here is what I found on the web:\n"
        for result in response.get('results', []):
            title = result.get('title', 'No Title')
            url = result.get('url', '#')
            content = result.get('content', '')[:300] # Limit length
            results_text += f"- {title}: {content} (Source: {url})\n"
            
        return results_text
        
    except Exception as e:
        return f"Error during web search: {str(e)}"
    
#rag is implemented here 

def execute_tool(tool_name: str, params: Dict[str, Any]) -> str:
    """
    Router calls this function to execute a specific tool.
    """
    # Map tool names to functions
    tools_map = {
        "web_search_cars": web_search_cars_tool,
        "search_inventory": search_inventory, 
    }
    
    tool_func = tools_map.get(tool_name)
    if not tool_func:
        return f"Tool {tool_name} not found."
    
    # --- Execute Web Search ---
    if tool_name == "web_search_cars":
        return tool_func(params.get("query", ""))

    # --- Execute Local Inventory ---
    if tool_name == "search_inventory":
        try:
            results = tool_func(
                budget_max=params.get('budget_max'),
                vehicle_type=params.get('vehicle_type'),
                fuel_type=params.get('fuel_type'),
                seating_min=params.get('seating_min'),
                brand=params.get('brand')
            )
            
            if not results:
                return "No matching cars found in local inventory."
            
            text_output = "Found these cars in our LOCAL STOCK:\n"
            for car in results:
                c_name = car.name if hasattr(car, 'name') else car.get('name', 'Unknown')
                c_price = car.price if hasattr(car, 'price') else car.get('price', 0)
                text_output += f"- {c_name}: ₹{c_price:,.0f}\n"
            return text_output
            
        except Exception as e:
            return f"Error searching inventory: {e}"

    return "Unknown tool requested."