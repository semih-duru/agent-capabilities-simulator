"""Configuration settings for the Agentic Platform Simulation Game."""
import os
from dotenv import load_dotenv

load_dotenv()

# Google Cloud Configuration
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
MODEL_NAME = "gemini-2.0-flash-exp"

# Game Configuration
INITIAL_BUDGET = 1000000  # $1M
INITIAL_TIME_WEEKS = 52  # 1 year
INITIAL_RESOURCES = 10  # team members

# Maturity Levels (0-100)
MATURITY_LEVELS = {
    "agent_development": 0,
    "agent_operations": 0,
    "data_platforms": 0,
    "security": 0,
    "governance": 0
}

# Thresholds for production readiness
PRODUCTION_READY_THRESHOLD = 60
MINIMUM_ACCEPTABLE_THRESHOLD = 40
