from phi.embedder.google import GeminiEmbedder
from phi.knowledge.website import WebsiteKnowledgeBase
from phi.vectordb.pgvector import PgVector

from tools.logger import logging


class WebKB:
    def __init__(self, KB_config: dict):
        self.urls = KB_config.get("urls", [])
        self.max_links = KB_config.get("max_links", 10)
        self.table_name = KB_config.get("table_name", "web_kb")
        self.db_url = KB_config.get(
            "db_url", "postgresql+psycopg://ai:ai@localhost:5532/ai"
        )
        self.embedder = GeminiEmbedder()
        logging.info(f"Initializing Web Knowledge Base with {[self.urls]}")
        self.knowledge_base = self.create_kb()
        logging.info(f"Web Knowdledge Base Initialized with {[self.urls]}")

    def create_kb(self):
        return WebsiteKnowledgeBase(
            urls=self.urls,
            max_links=self.max_links,
            vector_db=PgVector(
                table_name=self.table_name, db_url=self.db_url, embedder=self.embedder
            ),
        )

    def add_url(self, url: str):
        if url not in self.urls:
            self.urls.append(url)
            self.knowledge_base = self.create_kb()
            logging.info(f"Added URL {url} to Web Knowledge Base")
        else:
            logging.info(f"URL {url} already exists in Web Knowledge Base")

    def show_urls(self):
        logging.info(f"URLs in Web Knowledge Base: {self.urls}")
        return self.urls
    
    def get_kb(self):
        return self.knowledge_base
