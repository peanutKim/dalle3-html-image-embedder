from bs4 import BeautifulSoup, Comment
import imageGenerator, apiAuth


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

            # Generate the image and wait until it finishes
            imageGenerator.generateImage(image_desc, "{}.{}".format(image_desc, 'png'))

            # Define the HTML code to replace comments
            replacement_html = '<img src="images/{}.{}" alt="Random Image"> \n'.format(image_desc, 'png')

            # Convert the replacement HTML string to a BeautifulSoup object
            replacement_soup = BeautifulSoup(replacement_html, 'html.parser')

            # Replace the HTML comment with the new image generated
            comment.replace_with(replacement_soup)
        
        # Save the modified HTML back to the file
        with open(self.getFilePath(), 'w', encoding='utf-8') as file:
            file.write(str(soup))

if __name__ == "__main__":
    # image = TextToImage('htmls/mock.html')
    # image.read_and_replace()
    # varr = "Hello.png"
    # print('<img src="images/{}" alt="Random Image"> \n'.format(varr))
    # print(' image: very sour lemon '.split(':')[-1])
    # print(' image: very sour lemon '.split(':')[-1].strip(' '))