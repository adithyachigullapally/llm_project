Template for creating and submitting MAT496 capstone project.

# Overview of MAT496

In this course, we have primarily learned Langgraph. This is helpful tool to build apps which can process unstructured `text`, find information we are looking for, and present the format we choose. Some specific topics we have covered are:

- Prompting
- Structured Output 
- Semantic Search
- Retreaval Augmented Generation (RAG)
- Tool calling LLMs & MCP
- Langgraph: State, Nodes, Graph

We also learned that Langsmith is a nice tool for debugging Langgraph codes.

------

# Capstone Project objective

The first purpose of the capstone project is to give a chance to revise all the major above listed topics. The second purpose of the capstone is to show your creativity. Think about all the problems which you can not have solved earlier, but are not possible to solve with the concepts learned in this course. For example, We can use LLM to analyse all kinds of news: sports news, financial news, political news. Another example, we can use LLMs to build a legal assistant. Pretty much anything which requires lots of reading, can be outsourced to LLMs. Let your imagination run free.


-------------------------
# Note
Each phase contains multiple steps and is developed within a single working file.
I will upload the full code once an entire phase is completed, but I will update the README after every step.
-------------------------
# Project report Template

## Title: CarAstra Agent Network

## Overview
Overview: "AutoMate" is a voice-activated Agentic AI designed to revolutionize automotive consulting. Unlike static chatbots, it utilizes autonomous web tools to search the live internet for real-time global vehicle data, prices, and trends. The system features a unique "Personality Engine" that blends expert advice with humor and wit to drive high user engagement. Additionally, it implements Persistent Long-Term Memory, allowing the AI to remember user preferences and past conversations across sessions, creating a truly personalized, human-like, and addictive user experience.
## Reason for picking up this project

Expain how this project is aligned with this course content.
Prompting: I use advanced system prompts to define the "Global Concierge" persona, enforcing strict behavioral constraints (like "never guess prices") while injecting a witty, addictive personality into the AI.

Structured Output: All internal data flows through strict Pydantic models (JSON schema) to ensure that complex search parameters and conversation states are passed cleanly between nodes without errors.

Semantic Search: I utilize vector embeddings to process natural language queries, allowing the system to understand the intent behind vague requests (e.g., "safe car for new parents") rather than relying on exact keyword matching.

RAG (Retrieval Augmented Generation): Unlike static bots, I implemented a Web-RAG system where the model autonomously retrieves real-time data from the live internet and feeds it to the LLM to ensure up-to-the-minute accuracy.

Tool Calling & MCP: The model autonomously decides when to trigger the web_search tool to fetch facts or the TTS engine to speak, effectively giving the AI "hands" to execute Python code.

LangGraph (State, Nodes, Graph): The entire application is built on a StateGraph with specific nodes for reasoning and execution, managing the cyclic flow of conversation and maintaining long-term memory across sessions.

Here is the concise, 3-4 line version:

chose this project to go beyond static chatbots and build a humorous, active Voice-AI that actually "thinks" and searches the live web. My main goal was to prove that LangGraph is the future of voice assistants. I wanted to demonstrate that graph-based agents handle complex reasoning and memory much better than old linear models. Although this is just a prototype, it successfully provided a strong foundation for what intelligent, voice-controlled systems can become in the future
## Plan

I plan to excecute these steps to complete my project.

## 🗺️ Implementation Roadmap

### Phase 1: Environment & Infrastructure Setup
- [done] Step 1 involves initializing the project repository and defining the modular folder structure (`agents/`, `rag/`, `graph/`).
- [done] Step 2 involves configuring the Python virtual environment and installing core AI dependencies (`LangGraph`, `LangChain`, `OpenAI`).
- [done] Step 3 involves setting up secure environment variable management (`.env`) for API keys and configuration settings.

### Phase 2: Data Modeling & Schema Design(this phase takes place in one file so will upload the code after the whole phase is done)
- [todo] Step 4 involves designing Pydantic models to strictly define the `ConversationState` and `Message` history.
- [TODO] Step 5 involves creating structured output schemas for `InventorySearchRequest` to ensure type-safe tool execution.
- [TODO] Step 6 involves implementing the `CustomerProfile` schema to track user preferences and budget across the session.

### Phase 3: The "Brain" (LangGraph Architecture)
- [TODO] Step 7 involves designing the **StateGraph** architecture, defining the flow between the Reasoning Node and the Tool Node.
- [TODO] Step 8 involves implementing the **Concierge Node**, which serves as the central reasoning engine for the agent.
- [TODO] Step 9 involves building the **Cyclic Router Logic** that allows the agent to loop between thinking, searching, and speaking.
- 
  ### Phase 4: Intelligence & Tooling (RAG)
- [TODO] Step 10 involves implementing the **Semantic Search Engine** using vector embeddings to understand user intent (e.g., "safe family car").
- [TODO] Step 11 involves integrating the **Web Search Tool** (`duckduckgo-search`) to enable real-time fetching of global car prices and specs.
- [TODO] Step 12 involves binding the Python tools to the LLM, giving the agent the autonomous ability to "pause and search" the internet.

### Phase 5: Persona & Prompt Engineering
- [TODO] Step 13 involves engineering the `GLOBAL_EXPERT_PROMPT` to enforce constraints (e.g., "Never guess prices").
- [TODO] Step 14 involves injecting the **"Personality Engine"** to add humor, wit, and a casual tone to the AI's responses.

### Phase 6: Voice Interface Integration
- [TODO] Step 15 involves implementing the **Speech-to-Text (STT)** pipeline using Google Speech Recognition for accurate listening.
- [TODO] Step 16 involves implementing the **Text-to-Speech (TTS)** pipeline using `pyttsx3` for natural voice output.
- [TODO] Step 17 involves synchronizing the Voice I/O loop with the LangGraph processing speed to minimize latency.
- [TODO]step 18 involves stopping the AI when the user starts speaking.

  ### Phase 7: Visualization & Deployment (LangSmith)
- [TODO] Step 19 involves creating the `langgraph.json` configuration file to define the graph entry point and dependencies.
- [TODO] Step 20 involves setting up **LangSmith Tracing** to log all agent steps, tool calls, and errors for debugging.
- [TODO] Step 21 involves launching the **LangGraph Studio** using the `langgraph dev` command to visualize the agent's graph and interact with it in a GUI.
- [TODO] Step 22 involves conducting final edge-case testing and finalizing the project documentation.



more steps will bee added as i go on and solve it....


## Conclusion:
