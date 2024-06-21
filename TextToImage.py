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
        '''
        '''
        with open(self.getFilePath(), 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract comments
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))

        # Replace all comments with the appropriate replacement_html
        for comment in comments:
            image_desc = self.parseComment(comment)
            sanitized_desc = imageGenerator.sanitizePrompt(image_desc)
            

            # Generate the image and wait until it finishes
            imageGenerator.generateImage(image_desc, sanitized_desc)

            # Define the HTML code to replace comments
            replacement_html = f'<img src="images/{sanitized_desc}" alt="Random Image"> \n'

            # Convert the replacement HTML string to a BeautifulSoup object
            replacement_soup = BeautifulSoup(replacement_html, 'html.parser')

            # Replace the HTML comment with the new image generated
            comment.replace_with(replacement_soup)
        
        # Save the modified HTML back to the file
        with open(self.getFilePath(), 'w', encoding='utf-8') as file:
            file.write(str(soup))

if __name__ == "__main__":
    image = TextToImage('mock.html')
    image.read_and_replace()