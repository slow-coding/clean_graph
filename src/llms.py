import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("LLM_API_BASE"),
    model=os.getenv("LLM_MODEL"),
    api_key=SecretStr(
        os.getenv("LLM_API_KEY"),
    ),
    streaming=True,
)
