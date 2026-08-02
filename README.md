# Jijnasa-AI
MULTI AGENT RESEARCH AGENT

Multi-Agent Research Assistant a fully autonomous AI system that thinks,
searches, reads and writes on its own. Instead of a single AI answering your question from tools,
we are deploying a team of specialized intelligent agents that collaborate together to produce a professional
research report on any topic you give them. The Search Agent goes out on the live internet and finds the
most relevant and recent sources. The Reader Agent then dives deep into those sources, scraping and extracting
meaningful content. The Writer Agent takes all that gathered intelligence and crafts a well-structured, detailed report.
And finally the Critic Agent reviews the entire report, scores it and gives feedback just like a senior researcher
reviewing a junior's work. Every single agent is powered by a Large Language Model, connected through LangChain's
modern LCEL pipeline, and orchestrated through a shared memory system that makes them work as one unified brain.


LEVEL 1:
🌟 Features
Multi-Agent Architecture: Specialized agents for searching, reading, writing, and critiquing
Automated Web Research: Intelligent web search with Tavily API
Smart Content Extraction: Advanced web scraping with multiple fallback strategies
AI-Powered Report Generation: Automatically generates structured research reports
Quality Evaluation: Built-in critic agent for report validation and scoring
Interactive UI: Streamlit-based user interface for easy interaction
Pipeline Orchestration: Seamless coordination of multiple agents


ARCHITECTURE OF LEVEL 1:
┌─────────────────────────────────────────────────────┐
│           Streamlit UI (app.py)                     │
│      Multi-Agent Research Assistant Interface       │
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────┐
│      Research Pipeline (pipeline.py)                │
│        Orchestrates multi-agent workflow            │
└──────────────────┬──────────────────────────────────┘
                   │
    ┌──────────────┼──────────────┐
    │              │              │
┌───▼───┐    ┌────▼─────┐   ┌───▼────┐
│Search │    │   Reader  │   │ Writer │
│Agent  │    │   Agent   │   │ Chain  │
└───┬───┘    └────┬─────┘   └───┬────┘
    │             │             │
    │  ┌──────────▼─────────┐   │
    └─▶│  Tools Layer       │◀──┘
       │                    │
       │ • web_search      │
       │ • scrape_url      │
       │                    │
       └────────┬───────────┘
                │
            ┌───▼────────┐
            │ Critic     │
            │ Chain      │
            └────────────┘


WORKFLOW LEVEL 1 :

User Input: Enter a research topic via UI or script
Search Phase: Search agent queries the web using Tavily
Reading Phase: Reader agent extracts content from relevant URLs
Writing Phase: Writer chain synthesizes findings into a structured report
Review Phase: Critic chain evaluates the report and provides scores
Output: Display final report with feedback and scores

