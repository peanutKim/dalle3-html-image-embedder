from bs4 import BeautifulSoup, Comment
import imageGenerator

class TextToImage:
    """
    A class to read an HTML file, identify comments prefixed with 'image:', generate images based on these comments,
    and replace the comments with HTML image tags pointing to the generated images.
    """

    def __init__(self, file_path: str):
        """
        Initializes the TextToImage object with a file path.

        Parameters:
        - file_path (str): The path to the HTML file to be processed.
        """
        self.file_path = file_path
    
    def getFilePath(self):
        """
        Returns the file path associated with this TextToImage instance.

        Returns:
        - str: The file path.
        """
        return self.file_path
    
    def parseComment(self, comment: str):
        """
        Extracts the descriptive part of a comment following the 'image:' prefix.

        Parameters:
        - comment (str): The comment string to be parsed.

        Returns:
        - str: The descriptive part of the comment.
        """
        return comment.split(':')[-1].strip(' ')

    def read_and_replace(self):
        """
        Reads the HTML file, identifies comments prefixed with 'image:', generates images based on these comments,
        replaces the comments with HTML image tags, and saves the modified HTML back to the file.
        """
        with open(self.getFilePath(), 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract comments and filter only those starting with "image:"
        comments = soup.find_all(string=lambda text: isinstance(text, Comment) and text.strip().startswith('image:'))

        # Collect all image descriptions
        image_descs = [self.parseComment(comment) for comment in comments]
        sanitized_descs = [imageGenerator.sanitizePrompt(desc) for desc in image_descs]

        # Generate all images at once
        imageGenerator.generateImages(image_descs)

        # Insert the appropriate replacement_html under each comment
        for comment, sanitized_desc in zip(comments, sanitized_descs):
            # Insert the new image tag directly after the comment with a newline
            replacement_html = f'\n<img src="images/{sanitized_desc}" alt="Random Image">'

            # Convert the replacement HTML string to a BeautifulSoup object, including the newline
            replacement_soup = BeautifulSoup(replacement_html, 'html.parser')

            # Insert the new image tag and newline directly after the comment
            comment.insert_after(replacement_soup)

            # Remove 'image:' from the comment
            new_comment_text = str(comment).replace('image:', '').strip()
            comment.replace_with(Comment(new_comment_text))
        
        # Save the modified HTML back to the file
        with open(self.getFilePath(), 'w', encoding='utf-8') as file:
            file.write(str(soup))

#if __name__ == "__main__":
#    """
#    Main execution point of the script. Creates a TextToImage instance for a mock HTML file and processes it.
#    """
#    image = TextToImage('mock.html')
#    image.read_and_replace()