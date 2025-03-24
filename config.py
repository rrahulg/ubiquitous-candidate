WEB_SEARCH_AGENT = {
    "name": "web search agent",
    "role": "Searche the web for information.",
    "tools": [],  # make changes to the ./agents/web_search_agent.py file instead
    "instructions": [
        "only return factual information",
        "do not return opinions",
    ],
    "show_tool_calls": True,
    "markdown": True,
    "add_refrence": True,
    "prevent_hallucinations": True,
}
WEBSITE_KB = {
    "urls": ["https://docs.phidata.com/introduction"],
    "max_links": 10,
    "table_name": "website_documents",
    "db_url": "postgresql+psycopg://ai:ai@localhost:5532/ai",
}
