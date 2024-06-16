from openai import OpenAI

my_api_key = "enter your api key here"

def authGPT() -> OpenAI:
    client = OpenAI(api_key = my_api_key )
    return client