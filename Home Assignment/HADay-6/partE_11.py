# Part E: Code & Scope Logic
# 11.Local vs Global Debugging
# Create a global variable x = 50
# Define function that modifies x locally
# Define another that uses global x
# Print x before and after both functions
# Global variable
x = 50

def modify_local():
    x = 25  # This x is local to modify_local
    print("Inside modify_local, x =", x)

def use_global():
    global x
    x = x + 10  # Modifies the global x
    print("Inside use_global, x =", x)

print("Before any function call, x =", x)
modify_local()
print("After modify_local, x =", x)
use_global()
print("After use_global, x =", x)