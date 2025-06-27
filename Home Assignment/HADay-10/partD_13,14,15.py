# Part D: Real-World Tasks
# 13.Email Validator (Basic)
# Input a string and check if it contains '@' and ends with ".com"
# Input an email address
email = input("Enter an email address: ")
if "@" in email and email.endswith(".com"):
    print("Valid email format")
else:
    print("Invalid email format")

# 14.Censor Bad Words
# Input a sentence and replace "bad" and "ugly" with "***"
sentence = input("Enter a sentence: ")
censored = sentence.replace("bad", "***").replace("ugly", "***")
print("Censored sentence:", censored)

# 15.Format Name
# Input a name like "john DOE" and convert it to "John Doe" (use title())
name = input("Enter a name: ")
formatted_name = name.title()
print("Formatted Name:", formatted_name)