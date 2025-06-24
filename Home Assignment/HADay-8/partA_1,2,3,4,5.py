# Part A: Tuples – Creating, Accessing, and Use
# 1.Create a tuple t1 = (10, 20, 30, 40, 50)
# Print the first and last elements
# Print elements from index 1 to 3
# 2.Create a tuple with mixed data types:
# person = ("Alice", 25, 5.4, "Engineer")
# 3.Try changing an element in the tuple above and note what error is shown.
# 4.Use a loop to print all elements of t1.
# 5.Create a tuple with one item only:
# Example: t = ("Python",)
# (Why is the comma necessary?)

#Tuples – Creating, Accessing, and Use
# 1.Create a tuple t1 = (10, 20, 30, 40, 50)
# Print the first and last elements
# Print elements from index 1 to 3
t1 = (10, 20, 30, 40, 50)
print("First: ",t1[0])
print("Last: ",t1[-1])
print("index 1 to 3: ",t1[1:4])

# 2.Create a tuple with mixed data types:
# person = ("Alice", 25, 5.4, "Engineer")
person = ("Alice", 25, 5.4, "Engineer")
print(person)

#3.Try changing an element in the tuple above and note what error is shown.
person[1] = 30

# 4.Use a loop to print all elements of t1.
for item in t1:
    print(item)

#5.Create a tuple with one item only:
# Example: t = ("Python",)
# (Why is the comma necessary?)
item = ("sumedh",)
print(type(item))