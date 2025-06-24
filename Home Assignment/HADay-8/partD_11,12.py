#  Part D: Set Operations
# 11.Given:
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# Perform and print:
# Union of a and b
# Intersection of a and b
# Difference: a - b and b - a
# 12.Remove an element from a set using remove() and discard().
# Try removing an element that doesn’t exist using both

#1.Given:
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# Perform and print:
# Union of a and b
# Intersection of a and b
# Difference: a - b and b - a
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union
print("Union:", a.union(b))  # or a | b

# Intersection
print("Intersection:", a.intersection(b))  # or a & b

# Difference: a - b
print("a - b:", a.difference(b))  # or a - b

# Difference: b - a
print("b - a:", b.difference(a))  # or b - a

# 12.Remove an element from a set using remove() and discard().
# Try removing an element that doesn’t exist using both
s = {1, 2, 3, 4}

# remove() — throws an error if item not found
s.remove(2)  # Works fine
# s.remove(10)  # Uncommenting this will raise a KeyError

# discard() — does nothing if item not found
s.discard(3)  # Removes 3
s.discard(10)  # No error

print(s)