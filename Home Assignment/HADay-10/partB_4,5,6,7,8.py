# Part B: String Methods Practice
# 4.split() Method
# Input: "apple,banana,cherry"
# oSplit the string by comma and print the list.
fruits = "apple,banana,cherry"
fruits_list = fruits.split(',')
print(fruits_list)


# 5.join() Method
# Given a list: ["red", "green", "blue"]
# oJoin the list using - as separator: "red-green-blue"
colors = "red","green","blue"
joined_colors = "-".join(colors)
print(joined_colors)

# 6.replace() Method
# Input: "The sky is blue"
# oReplace "blue" with "clear"
sen = "The sky is Blue"
updated_sen = sen.replace("blue","clear")
print("Updated Sentence: ",updated_sen)

# 7.lower() and upper()
# oConvert "Python Is FUN" to all lowercase and all uppercase.
sentence = "Python Is FUN"
lower_sen = sentence.lower()
upper_sen = sentence.upper()
print("LowerCase: ",lower_sen)
print("UpperCase: ",upper_sen)

# 8.count() and find()
# For the string "banana":
# oCount how many times "a" appears
word = "banana"
a_count = word.count("a")
a_find_index = word.find("a")
print(f"Count of 'a' in banana is: {a_count}")
print(f"a found at Index: {a_find_index}")
