#partC:Modifying Elements
# 6.Replace the third element of a list marks = [45, 67, 89, 34] with 99.
# 7.Add an element "python" at the end of a list languages = ["C", "Java"].
# 8.Insert "HTML" at index 1 in the above list.
# 9.Remove the last item using pop() and print it.
# 10.Delete the second element using del.

#6.Replace the third element of a list marks = [45, 67, 89, 34] with 99.
marks = [45, 67, 89, 34]
marks[2] = 99
print("Updated marks:", marks)

#7.Add an element "python" at the end of a list languages = ["C", "Java"].
languages = ["C", "Java"]
languages.append("python")
print("Languages after appending:", languages)

# 8.Insert "HTML" at index 1 in the above list.
languages.insert(1,"HTML")
print("Languages after inserting:",languages)

# 9.Remove the last item using pop() and print it.
last_item = languages.pop()
print("Popped item:", last_item)
print("Languages after pop:", languages)

# 10.Delete the second element using del.
del languages[1]
print("Final List: ",languages)
