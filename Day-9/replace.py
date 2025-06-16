text = "cat dog cat rat dog cat"
words = text.split()

result = [str(words.count(word))for word in words]
output = " ".join(result)

print(output)