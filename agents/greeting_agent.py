import os
import re

from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq

from tools.logger import logging

load_dotenv()


class GreetingAgent:
    def __init__(self, agent_config: dict):
        self.name = agent_config.get("name", "GreetingAgent")
        self.role = agent_config.get(
            "role", "you need to greet the user or bid them goodbye based on the input"
        )
        self.model = Groq(
            id="DeepSeek-R1-Distill-Llama-70B", api_key=os.getenv("GROQ_API_KEY")
        )

        self.agent = Agent(
            name=self.name,
            role=self.role,
            model=self.model,
        )
        logging.info(f"{self.name} initialised")

    def start(self, message="hello"):
        response = self.agent.run(message)
        cleaned_response = re.sub(
            r"<think>.*?</think>\n*", "", response.content, flags=re.DOTALL
        ).strip()
        return cleaned_response
