import os
import re
import sys

from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.googlesearch import GoogleSearch

from tools.logger import CustomException, logging

load_dotenv()
logging.info("Reading environment variables...")
groq_api = os.getenv("GROQ_API_KEY")
logging.info("Groq API key loaded successfully!")


class WebSearchAgent:
    def __init__(self, agent_config: dict):
        self.name = agent_config.get("name", "web search agent")
        self.role = agent_config.get("role", "Search the web for information.")
        self.tools = [GoogleSearch()]
        self.instructions = agent_config.get(
            "instructions", "search the web for accurate information"
        )
        self.show_tool_calls = agent_config.get("show_tool_calls", True)
        self.markdown = agent_config.get("markdown", True)
        self.prevent_hallucinations = agent_config.get("prevent_hallucinations", True)
        self.add_references = agent_config.get("add_references", True)
        self.model = Groq(id="DeepSeek-R1-Distill-Llama-70B", api_key=groq_api)

        self.agent = Agent(
            name=self.name,
            role=self.role,
            tools=self.tools,
            instructions=self.instructions,
            show_tool_calls=self.show_tool_calls,
            markdown=self.markdown,
            prevent_hallucinations=self.prevent_hallucinations,
            add_references=self.add_references,
            model=self.model,
        )
        logging.info("INITIALISED web search agent")

    def search(self, query: str) -> str:
        """
        Perform a web search using the agent and return the response.

        :param query: The search query string.
        :return: The search result as a string.
        """
        logging.info(f"🔍 Searching for: {query}")
        try:
            response = self.agent.run(query)
            # cleaned_response = re.sub(
            #     r"<think>.?</think>\n", "", response.content, flags=re.DOTALL
            # ).strip()
            # logging.info("Query result: ", cleaned_response)
            return response
        except Exception as e:
            error_message = f"Error during search: {str(e)}"
            logging.error(error_message)
            raise CustomException("Search operation failed", sys)
