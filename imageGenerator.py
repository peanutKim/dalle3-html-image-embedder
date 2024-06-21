import os
import requests
from apiAuth import authGPT
import re

client = authGPT()


def sanitize_filename(prompt: str, max_length: int = 50) -> str:
    """
    Sanitizes and shortens the prompt to be used as a filename.

    Parameters:
    - prompt (str): The prompt to sanitize.
    - max_length (int): Maximum length of the filename.

    Returns:
    - (str): A sanitized and shortened version of the prompt suitable for use as a filename.
    """
    # Remove or replace characters not allowed in filenames
    sanitized = re.sub(r'[<>:"/\\|?*]', '', prompt)
    # Replace spaces with underscores
    sanitized = sanitized.replace(' ', '_')
    # Shorten to the maximum length
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    return sanitized


def generateImage(prompt: str, image_name: str):
    """
    Generates an image based on a given prompt and saves it with a specified image name.

    Parameters:
    - prompt (str): The prompt to generate the image from.
    - image_name (str): The name of the file to save the image as, including its extension.

    The function saves the generated image in a directory named 'images' located in the same
    directory as this script. If the 'images' directory does not exist, it is created.
    """
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url

    # Use the provided image_name for the file name
    image_path = os.path.join(os.path.dirname(__file__), 'images', image_name)

    # Ensure the images directory exists before saving
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    # Download and save the image
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open(image_path, 'wb') as file:
            file.write(image_response.content)


def generateImages(prompts: list):
    """
    Generates and saves images for a list of prompts with descriptive filenames.

    Parameters:
    - prompts (list): A list of strings, where each string is a prompt to generate an image from.
    """
    for _, prompt in enumerate(prompts):
        # Use a sanitized and shortened version of the prompt for the filename
        filename = f"{sanitize_filename(prompt)}.png"
        generateImage(prompt, filename)

if __name__ == "__main__":
   prompts = [
        "a cute cat with a hat",
        "cute anime girl with a sword",
   ]
   generateImages(prompts)