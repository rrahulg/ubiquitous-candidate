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

EMAIL_AGENT = {
    "name": "Email Agent",  # Name of the agent (e.g., "EmailAgent")
    "role": "Send an email to the selected candidate",  # Role of the agent (e.g., "Send Email to the Selected Candidate")
    "receiver_email": "",  # Recipient's email address
    "sender_email": "",  # Sender's email address
    "sender_name": "",  # Sender's name
    "markdown": True,  # Enable Markdown formatting (default: True)
    "verbose": True,  # Enable verbose mode (default: True)
}

GREETING_AGENT = {
    "name": "Greeting agent",
    "role": "You need to greet the user or bid them goodbye based on the input",
}
KNOWLEDGE_BASE_AGENT = {
    "name": "Knowledge Base Agent",
    "role": "Answer the query from the given knowledge base",
    "instruction": ["Search the knowledge base for information"],
    "knowledge_base": None,
    "search_knowledge": True,
    "markdown": True,
    "prevent_hallucination": True,
}
WEBSITE_KB = {
    "urls": ["https://docs.phidata.com/introduction"],
    "max_links": 10,
    "table_name": "website_documents",
    "db_url": "postgresql+psycopg://ai:ai@localhost:5532/ai",
}
import os

JSON_KB = {
    "path": os.getcwd() + r"\data\data.json",
    "table_name": "ai.json_documents",
    "db_url": "postgresql+psycopg://ai:ai@localhost:5532/ai",
}
DATAGEN = {
    "data_path": os.getcwd() + r"\data\resumes",
    "output_path": os.getcwd() + r"\data\data.json",
    "system_prompt": "You are a data generator. You will be given a set of resumes and you need to generate a json file from it.",
    "model": "gemini-2.0-pro-exp-02-05",
    "generative_config": {
        "temperature": 0.6,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
    },
}
