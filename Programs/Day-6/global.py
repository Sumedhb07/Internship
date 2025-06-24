#local variable 
a=50
def local():
    a=51
    print(a)
print(a)
print(f"local Variable : {a}")
local()
