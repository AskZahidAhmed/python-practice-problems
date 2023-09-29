import re
from bs4 import BeautifulSoup

def count_words_in_file(file_path, is_html=False):
    with open(file_path, 'r') as file:
        content = file.read()

    if is_html:
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text()
    else:
        text = content
    words = re.findall(r'\w+', text)
    word_count = len(words)
    return word_count

# File paths
html_file_path = 'file_with_html.txt'
text_file_path = 'file_without_html.txt'

# Count words in HTML file
html_word_count = count_words_in_file(html_file_path, is_html=True)
print(f"Word count in HTML file: {html_word_count}")

# Count words in text file
text_word_count = count_words_in_file(text_file_path)
print(f"Word count in text file: {text_word_count}")

