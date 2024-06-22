import os
import subprocess
import requests
from apiAuth import authGPT
import re

client = authGPT()

def sanitizePrompt(prompt: str, max_length: int = 50) -> str:
    """
    Cleans up the prompt for use as a filename by removing invalid characters and limiting its length. Adds '.png' extension.

    Parameters:
    - prompt (str): The input prompt.
    - max_length (int): The maximum allowed length for the filename (excluding '.png').

    Returns:
    - str: A clean, shortened filename ending with '.png'.
    """
    # Eliminate invalid filename characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '', prompt)
    # Convert spaces to underscores
    sanitized = sanitized.replace(' ', '_')
    # Truncate to max_length if necessary
    if len(sanitized) > max_length - 4:  # Account for '.png'
        sanitized = sanitized[:max_length - 4]
    # Append file extension
    sanitized += '.png'
    return sanitized

def generateImage(prompt: str, image_name: str):
    """
    Creates an image from a prompt and saves it with the given filename.

    Parameters:
    - prompt (str): The inspiration for the image.
    - image_name (str): The filename for the saved image, including its extension.

    Saves the image in an 'images' directory within the script's directory. Creates the directory if it doesn't exist.
    """
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url

    github_workspace = os.getenv('GITHUB_WORKSPACE', os.path.dirname(__file__))
    image_path = os.path.join(github_workspace, 'images', image_name)
    
    # Create 'images' directory if missing
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    # Download the image and save it
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open(image_path, 'wb') as file:
            file.write(image_response.content)

def generateImages(prompts: list):
    """
    Processes a list of prompts to generate and save images with appropriate filenames.

    Parameters:
    - prompts (list): Prompts for image generation.
    """
    for prompt in prompts:
        # Filename from sanitized prompt
        filename = sanitizePrompt(prompt)
        generateImage(prompt, filename)