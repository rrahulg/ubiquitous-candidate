import os
import sys

from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq

from tools.logger import CustomException, logging

load_dotenv()
logging.info("Reading environment variables...")
groq_api = os.getenv("GROQ_API_KEY")
logging.info("Groq API key loaded successfully!")


class KBAgent:
    def __init__(self, agent_config: dict):
        self.name = agent_config.get("name", "knowledge base agent")
        self.role = agent_config.get(
            "role", "You are an agent who answers based on the knowledge base."
        )
        self.instructions = agent_config.get(
            "instructions", "search the knowledge base for information"
        )
        self.knowledge_base = agent_config.get("knowledge_base")
        if self.knowledge_base is None:
            logging.info("Knowldge base is empty")
        self.search_knowledge = agent_config.get("search_knowledge", True)
        self.model = Groq(id="DeepSeek-R1-Distill-Llama-70B", api_key=groq_api)
        self.markdown = agent_config.get("markdown", True)
        self.prevent_hallucinations = agent_config.get("prevent_hallucinations", True)

        self.agent = Agent(
            name=self.name,
            role=self.role,
            instructions=self.instructions,
            search_knowledge=self.search_knowledge,
            model=self.model,
            knowledge_base=self.knowledge_base,
            markdown=self.markdown,
            prevent_hallucinations=self.prevent_hallucinations,
        )
        logging.info("INITIALISED knowledge base agent")
        self.agent.knowledge.load(recreate=False)

    def search(self, query: str) -> str:
        logging.info(f"🔍 Searching for: {query}")
        try:
            response = self.agent.run(query)
            if hasattr(response, "content"):
                result = response.content.strip()
                logging.info(f"✅ Search Result: {result}")
                return result
            else:
                logging.info("Search doesnt have content")
                logging.info(f"Search result:{response}")
                return response
        except Exception as e:
            raise CustomException("Search Operation Failed", sys)
