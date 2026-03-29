import os
from dotenv import load_dotenv

load_dotenv()


ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-latest")

MAX_CLASSIFIER_TOKENS = 250
CLASSIFIER_TEMPERATURE = 0.0


if not ANTHROPIC_API_KEY:
    raise ValueError(
        "ANTHROPIC_API_KEY is not set. Please add it to your .env file."
    )