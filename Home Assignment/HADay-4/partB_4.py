# 4.Take temperature as input and:
# If temp > 35, print "Too Hot"
# If 25–35, print "Normal Weather"
# If 15–24, print "Cool"
# Else, print "Too Cold"
# Ask the user to enter the temperature
temperature = float(input("Enter the temperature: "))

# Determine the weather condition
if temperature > 35:
    print("Too Hot")
elif 25 <= temperature <= 35:
    print("Normal Weather")
elif 15 <= temperature <= 24:
    print("Cool")
else:
    print("Too Cold")