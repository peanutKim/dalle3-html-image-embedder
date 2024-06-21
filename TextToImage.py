from bs4 import BeautifulSoup, Comment
import imageGenerator


class TextToImage:
    '''
    '''
    def __init__(self, file_path: str):
        '''
        '''
        self.file_path = file_path
    
    def getFilePath(self):
        return self.file_path
    
    def parseComment(self, comment: str):
        '''
        Returns a string of the desired input
        '''

        return comment.split(':')[-1].strip(' ')

    def read_and_replace(self):
        with open(self.getFilePath(), 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract comments
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))

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

if __name__ == "__main__":
    image = TextToImage('mock.html')
    image.read_and_replace()