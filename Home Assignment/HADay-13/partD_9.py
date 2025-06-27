# **Part D: Understanding __name__ == "__main__"
# 9.Create a file count_words.py:
# oDefines a function count_words(sentence).
# oIf run directly (if __name__ == "__main__":), ask the user for a sentence and print the word count.
# oImport this module in another script and use count_words().
# count_words.py

def count_words(sentence):
    """Returns the number of words in a sentence."""
    return len(sentence.split())

# Run directly
if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    print("Word count:", count_words(user_input))