from openai import OpenAI
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Access the API key from environment variables
my_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = my_api_key )

response = client.images.generate(
  model="dall-e-3",
  prompt="anime girl drinking beer",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)