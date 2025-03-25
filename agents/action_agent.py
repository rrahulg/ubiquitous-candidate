import os
import sys

from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.email import EmailTools

from tools.logger import CustomException, logging

load_dotenv()


class EmailAgent(Agent):
    def __init__(self, agent_config: dict):
        self.name = agent_config.get("name", "EmailAgent")
        self.role = agent_config.get("role", "Send Email to the Selected candidate")
        self.markdown = True
        self.reciever_email = agent_config.get("reciever_email")
        self.sender_email = agent_config.get("sender_email")
        self.sender_password = os.getenv("password")
        self.sender_name = agent_config.get("sender_name")
        self.model = Groq(
            id="DeepSeek-R1-Distill-Llama-70B", api_key=os.getenv("GROQ_API_KEY")
        )

        self.agent = Agent(
            name=self.name,
            role=self.role,
            markdown=self.markdown,
            model=self.model,
            tools=[
                EmailTools(
                    receiver_email=self.reciever_email,
                    sender_email=self.sender_email,
                    sender_name=self.sender_name,
                    sender_passkey=self.sender_password,
                )
            ],
            verbose=True,
        )
        logging.info("INITIALISED Email Agent")

    def send_email(self, subject: str, body: str):
        logging.info(f"Sending email to {self.reciever_email}")
        try:
            response = self.agent.run(
                f"send an email to {self.reciever_email} with subject '{subject}' and body '{body}'"
            )
            logging.info(f" Email sent to {self.reciever_email}")
            return response
        except Exception as e:
            logging.error(f" Email sending failed to {self.reciever_email}")
            raise CustomException("Email Sending Failed", sys)
