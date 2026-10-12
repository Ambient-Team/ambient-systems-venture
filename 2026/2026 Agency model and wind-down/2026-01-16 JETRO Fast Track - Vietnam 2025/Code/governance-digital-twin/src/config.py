"""
Configuration management for Governance Digital Twin.
Loads from .env and provides typed configuration objects.
"""

import os
import logging
from typing import Optional
from pydantic import BaseSettings, Field
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Neo4jConfig(BaseSettings):
    """Neo4j database configuration."""
    uri: str = Field(default="bolt://localhost:7687", env="NEO4J_URI")
    username: str = Field(default="neo4j", env="NEO4J_USERNAME")
    password: str = Field(default="password", env="NEO4J_PASSWORD")
    database: str = Field(default="neo4j", env="NEO4J_DATABASE")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


class LLMConfig(BaseSettings):
    """LLM (Large Language Model) configuration."""
    openai_api_key: Optional[str] = Field(default=None, env="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-4", env="OPENAI_MODEL")
    gemini_api_key: Optional[str] = Field(default=None, env="GEMINI_API_KEY")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


class CrewAIConfig(BaseSettings):
    """CrewAI multi-agent configuration."""
    verbose: bool = Field(default=True, env="CREW_VERBOSE")
    max_retries: int = Field(default=3, env="CREW_MAX_RETRIES")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


class AppConfig(BaseSettings):
    """Application configuration."""
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    sandbox_mode: bool = Field(default=True, env="SANDBOX_MODE")
    data_anonymization: bool = Field(default=True, env="DATA_ANONYMIZATION")
    streamlit_port: int = Field(default=8501, env="STREAMLIT_PORT")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


class Settings:
    """Master settings class combining all configurations."""
    
    def __init__(self):
        """Initialize all configuration objects."""
        self.neo4j = Neo4jConfig()
        self.llm = LLMConfig()
        self.crewai = CrewAIConfig()
        self.app = AppConfig()
        
        # Validate critical settings
        self._validate()
    
    def _validate(self):
        """Validate critical configuration."""
        if not self.neo4j.uri:
            raise ValueError("NEO4J_URI must be set in .env")
        
        if not self.llm.openai_api_key and not self.llm.gemini_api_key:
            raise ValueError("Either OPENAI_API_KEY or GEMINI_API_KEY must be set")
        
        # Configure logging level
        log_level = getattr(logging, self.app.log_level, logging.INFO)
        logging.basicConfig(level=log_level)


# Global settings instance
settings = Settings()
