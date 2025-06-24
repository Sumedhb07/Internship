# Part C: Sets – Creating and Using
# 8.Create a set s1 = {1, 2, 3, 4, 5}
# oAdd the number 6
# oTry adding 3 again. What happens?
# 9.Create a set from a list with repeated values:
# numbers = [1, 2, 2, 3, 4, 4, 5]
# oUse set() to remove duplicates
# 10.Use a loop to print all items in a set.

# 8.Create a set s1 = {1, 2, 3, 4, 5}
# Add the number 6
# Try adding 3 again. What happens?
s1 = {1, 2, 3, 4, 5}
s1.add(6)
s1.add(3)
print(s1)

#9.Create a set from a list with repeated values:
# numbers = [1, 2, 2, 3, 4, 4, 5]
# oUse set() to remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)

#10.Use a loop to print all items in a set.
for item in s1:
    print(item)
