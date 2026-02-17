import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenRouter LLM (Free Nemotron Model)
# CrewAI's native LLM class is often more compatible with its agents
llm = LLM(
    model="openrouter/arcee-ai/trinity-large-preview:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.4
)
