import os
from TextToImage import TextToImage

def process_html_files(directory="."):
    """
    Processes all .html files in the specified directory and its subdirectories
    using the TextToImage class to replace 'image:' comments with actual image tags.

    Parameters:
    - directory (str): The path to the directory containing .html files to process.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}...")
                image_processor = TextToImage(file_path)
                image_processor.read_and_replace()

if __name__ == "__main__":
    process_html_files()