from bs4 import BeautifulSoup, Comment

# Path to your HTML file
file_path = 'htmls/mock.html'

# Open and read the file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Define the HTML code to replace comments
replacement_html = '<img src="images/mockImage.png" alt="Random Image"> \n'

# Convert the replacement HTML string to a BeautifulSoup object
replacement_soup = BeautifulSoup(replacement_html, 'html.parser')

# Extract comments
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

# Print comments
for comment in comments:
    print(comment)
    comment.replace_with(replacement_soup)


# Save the modified HTML back to the file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(str(soup))

# Naming Convention: <!-- image: sexy times -->
print("HTML file has been modified and saved.")