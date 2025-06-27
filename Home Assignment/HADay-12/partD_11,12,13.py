# 11.Custom Calculator
# Take two numbers and an operator as input.
# Perform the calculation inside try.
# Handle:
# oZeroDivisionError
# oValueError for bad input
# oException for invalid operators
try:
    # Take user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    # Perform the calculation based on the operator
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2  # Might raise ZeroDivisionError
    else:
        raise Exception("Invalid operator. Please use +, -, *, or /.")

    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print(f"Error: {e}")

# ATM Simulator
# Initial balance = 5000
# Ask user to withdraw an amount.
# If amount > balance, raise an exception with message "Insufficient balance".
# Always print "Transaction ended" in finally.
balance = 5000

try:
    amount = float(input("Enter the amount to withdraw: "))
    
    if amount > balance:
        raise Exception("Insufficient balance")
    
    balance -= amount
    print(f"Withdrawal successful. Remaining balance: {balance}")

except Exception as e:
    print(f"Error: {e}")

finally:
    print("Transaction ended.")

# 13.Loop Until Succe12.ss
# Ask the user to enter an integer.
# If invalid, catch the exception and repeat the question until the input is valid.
while True:
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)
        print(f"Thanks! You entered the integer: {number}")
        break  # Exit the loop if conversion is successful
    except ValueError:
        print("Invalid input. Please enter a valid integer.")