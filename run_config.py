from agents import AsyncOpenAI, OpenAIChatCompletionsModel, OpenAIProvider, RunConfig
from dotenv import load_dotenv
import os

load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")
url = "https://generativelanguage.googleapis.com/v1beta/openai/"

exter_client = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url= url
)

provider = OpenAIProvider(openai_client= exter_client)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client= exter_client
)

config = RunConfig(
    model= model,
    model_provider= provider,
    tracing_disabled= True
)