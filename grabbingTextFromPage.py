from bs4 import BeautifulSoup

# Import URL Module
import urllib.request

# Import NLTK Module
import nltk
from nltk.corpus import stopwords

# Set page from external url
response = urllib.request.urlopen('http://php.net')

# Reading html page from url
html = response.read()

# Format html like a text
soup = BeautifulSoup(html, "html.parser")

# Formatted text from html
text = soup.get_text(strip=True)

# Formatted text to split as token
tokens = [t for t in text.split()]

# Clean output tokens
cleans_token = tokens[:]

# Stop as English language
stopWords = stopwords.words('english')

# Clean tokens and stop word in english
for token in tokens:
    if token in stopwords.words('english'):
        cleans_token.remove(token)

print(str(token))
# # Count words frequency
# wordFrequency = nltk.FreqDist(tokens)
#
# # Iterate word frequency and show output
# for wordKeys,wordValues in wordFrequency.items():
#     print(str(wordKeys) + ':' + str(wordValues))
