#  Part C: Finally Block Use
# 6.Simulate Locking/Unlocking
# lock = False
# oIn try: set lock = True and simulate an error (e.g., 1 / 0)
# oIn finally: set lock = False and print "Resource released".
lock = False
try:
    lock = True
    print("Lock engaged.")
    # Simulate an error
    result = 1 / 0
except ZeroDivisionError:
    print("An error occurred during processing.")
finally:
    lock = False
    print("Resource released.")

# 7.File Always Closes
# oOpen a file (use open("sample.txt", "w")) in try.
# oWrite to it, raise an error manually using raise
# oIn finally, close the file and print "File closed".
try:
    file = open("sample.txt", "w")
    file.write("Writing some important data...\n")
    
    # Manually raise an error for testing
    raise RuntimeError("Something went wrong!")

except RuntimeError as e:
    print(f"Caught an error: {e}")

finally:
    file.close()
    print("File closed.")