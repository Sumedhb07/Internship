# 13.Word Replacer
# oFrom a file story.txt, replace the word "sad" with "happy"
# oSave the result to a new file updated_story.txt
# Open the original story file for reading
with open("story.txt", "r") as infile:
    content = infile.read()

updated_content = content.replace("sad", "happy")

with open("updated_story.txt", "w") as outfile:
    outfile.write(updated_content)

# 14.Merge Two Files
# oRead from file1.txt and file2.txt
# oMerge their contents and write to merged.txt
# Open both input files and read their contents
with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    content1 = file1.read()
    content2 = file2.read()

merged_content = content1 + "\n" + content2

# Write the combined content into merged.txt
with open("merged.txt", "w") as outfile:
    outfile.write(merged_content)

# 15.Email Extractor
# oFrom a text file containing a paragraph, extract all words containing '@' and save them as a list of emails to emails.txt
# Extract emails from a paragraph in 'input.txt' and save to 'emails.txt'
with open("input.txt", "r") as infile:
    words = infile.read().split()

emails = [word for word in words if "@" in word]

with open("emails.txt", "w") as outfile:
    for email in emails:
        outfile.write(email + "\n")