# 16.Find the Longest Word
# Input a sentence
# Find and print the longest word and its length
# Input a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = ""
max_length = 0
for word in words:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)
print("Longest word:", longest_word)
print("Length:", max_length)

# 17.Initials Generator
# Input: "John Ronald Reuel Tolkien"
# Output: "J.R.R.T."
# Input full name
full_name = input("Enter a full name: ")
words = full_name.split()
initials = ".".join([word[0].upper() for word in words]) + "."
print("Initials:", initials)

# 18.URL Parser
# Input a URL like "https://www.example.com/home"
# Extract and print:
# oDomain: example.com
# oPath: /home
# Import the urllib.parse module
from urllib.parse import urlparse
url = input("Enter a URL: ")
parsed_url = urlparse(url)
domain = parsed_url.netloc.replace("www.", "")
path = parsed_url.path
print("Domain:", domain)
print("Path:", path)