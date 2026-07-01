from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

DEFAULT_MODEL = "mistral-large-latest"

CONFIDENCE_THRESHOLD = 0.75
MAX_REASONING_POINTS = 5