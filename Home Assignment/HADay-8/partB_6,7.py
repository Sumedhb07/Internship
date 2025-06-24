# Part B: Tuple Use Cases
# 6.Store coordinates using a tuple:
# location = (19.0760, 72.8777) (latitude, longitude)
# oPrint each value separately.
# 7.Write a function get_min_max(numbers) that:
# oAccepts a list
# oReturns a tuple (min, max)

#6.Store coordinates using a tuple:
# location = (19.0760, 72.8777) (latitude, longitude)
# oPrint each value separately.
# Tuple with coordinates
location = (19.0760, 72.8777)

# Print each value separately
print("Latitude:", location[0])
print("Longitude:", location[1])

#7.Write a function get_min_max(numbers) that:
# Accepts a list
# Returns a tuple (min, max)
num = [8, 3, 15, 2, 9]
result =  get_min_max(num)
print("Minimum",result[0])
print("Maximum",result[1])







