from openai import OpenAI
from dotenv import load_dotenv
import os

def authGPT() -> OpenAI:
    # Load environment variables from .env file
    load_dotenv()

    # Access the API key from environment variables
    my_api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key = my_api_key )
    return client