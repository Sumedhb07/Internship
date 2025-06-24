lock = False
try:
    lock = True
    print("Lock aquired")
    result = 1 / 0
except ZeroDivisionError:
    print("zero cannot divide")
finally:
    lock = False
    print("lock Released")
    
     