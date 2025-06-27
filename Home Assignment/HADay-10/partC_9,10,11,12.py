# Part C: Logical String Tasks
# 9.Vowel Counter
# oInput a sentence and count how many vowels are present.
sentence = input("Enter a Sentence:- ")
vowel = "aeiouAEIOU"
vowel_count = 0
for char in sentence:
    if char in vowel:
        vowel_count += 1
        print("Number of Vowels in Sentence: ",vowel_count)

# 10.Palindrome Checker
# Check if a string is the same when reversed (e.g., "madam", "racecar")
# Input a string
text = input("Enter a word or phrase: ")
cleaned_text = text.replace(" ", "").lower()
if cleaned_text == cleaned_text[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

# 11.Word Count
# Input a sentence and print total number of words.
sentence = input("Enter a Sentence:- ")
words = sentence.split()
word_count = len(words)
print("Total number of words: ",word_count)


# 12.Character Frequency Dictionary
# Input a string and create a dictionary of character counts.
# Example: "book" → {'b':1, 'o':2, 'k':1}
# Input a string
text = input("Enter a string: ")
char_freq = {}
for char in text:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
print(char_freq)
