from openai import OpenAI
import os

def authGPT() -> OpenAI:
    # Access the API key directly from environment variables
    my_api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=my_api_key)
    return client