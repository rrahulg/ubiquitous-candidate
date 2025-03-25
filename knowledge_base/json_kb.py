from pathlib import Path

from phi.embedder.google import GeminiEmbedder
from phi.knowledge.json import JSONKnowledgeBase
from phi.vectordb.pgvector import PgVector

from tools.logger import logging


class JsonKB:
    def __init__(self, KB_config: dict):
        self.path = KB_config.get("path", "/data/kb.json")
        self.table_name = KB_config.get("table_name", "ai.json_documents")
        self.db_url = KB_config.get(
            "db_url", "postgresql+psycopg://ai:ai@localhost:5532/ai"
        )
        self.embedder = GeminiEmbedder()
        logging.info(f"Initializing JSON Knowledge Base with {[self.path]}")
        self.knowledge_base = self.create_kb()
        logging.info(f"JSON Knowledge Base Initialized with {[self.path]}")

    def create_kb(self):
        return JSONKnowledgeBase(
            path=self.path,
            vector_db=PgVector(
                table_name=self.table_name, db_url=self.db_url, embedder=self.embedder
            ),
        )

    def show_paths(self):
        logging.info(f"Paths in JSON Knowledge Base: {self.path}")
        return self.path

    def get_kb(self):
        logging.info("Returning JSON Knowledge Base")
        return self.knowledge_base
