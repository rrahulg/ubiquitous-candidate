import os
import sys

import config
from agents.action_agent import EmailAgent
from agents.kb_agent import KBAgent
from agents.web_search_agent import WebSearchAgent
from knowledge_base.json_kb import JsonKB
from tools.data_json_generator import Pdf_to_JSON as DataGenerator


def generate_candidate_json():
    print("Generating candidate data from resumes...")
    datagen_config = config.DATAGEN
    data = DataGenerator(datagen_config)
    data.generate_json()
    print("Resumes saved in JSON format.\n")


def get_user_choice():
    try:
        choice = int(
            input(
                "\nHello! How may I help you?\n"
                "1. Show current industry trends\n"
                "2. Fetch candidates based on job description\n"
                "3. Exit\n"
                "Enter your choice: "
            )
        )
        if choice not in [1, 2, 3]:
            raise ValueError
        return choice
    except ValueError:
        print("Invalid input. Please enter 1, 2, or 3.")
        return None


def handle_industry_trends():
    sector = input("Enter the job sector you would like to know about: ")
    websearch_config = config.WEB_SEARCH_AGENT
    web_agent = WebSearchAgent(websearch_config)
    answer = web_agent.search(
        f"What are the current industry trends in the {sector} sector?"
    )
    print(f"\nTop Trends in {sector}:\n{answer}\n")


def handle_candidate_search():
    jd = input("Please enter the job description: ")
    try:
        candidate_count = int(input("How many candidates do you want to fetch? "))
    except ValueError:
        print("Invalid number. Please enter a valid integer.")
        return

    # Load knowledge base
    jkb_config = config.JSON_KB
    jkb = JsonKB(jkb_config)
    jkb.get_kb()
    jkb.load()
    print("JSON knowledge base loaded successfully.")

    # Search candidates
    kb_agent_config = config.KNOWLEDGE_BASE_AGENT
    kb_agent = KBAgent(kb_agent_config)
    candidates = kb_agent.search(
        f"Find the top {candidate_count} candidates from the knowledge base for the job description: {jd}"
    )
    print(f"\nTop {candidate_count} matching candidates:\n{candidates}\n")

    # Email shortlisted candidates
    email_agent_config = config.EMAIL_AGENT
    email_agent = EmailAgent(email_agent_config)
    email_agent.send_email(
        subject="Job Application",
        body=(
            "Dear Candidate,\n\n"
            "We are pleased to inform you that you have been shortlisted for the position based on your resume.\n\n"
            "Best regards,\n[Your Company]"
        ),
    )
    print("Emails sent to shortlisted candidates.\n")


def main():
    generate_candidate_json()

    while True:
        choice = get_user_choice()
        if choice == 1:
            handle_industry_trends()
        elif choice == 2:
            handle_candidate_search()
        elif choice == 3:
            print("Thank you for using the AI Recruitment Assistant. Goodbye!")
            break


if __name__ == "__main__":
    main()
