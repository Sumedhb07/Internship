#global variable 
count=0
def glo():
    global count
    count+=3 
    print(count)
glo()
