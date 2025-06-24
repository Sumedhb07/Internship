#find no of letter from string  
count=0
def str(name):
    global count
    for i in name :
        if i=="s":
            count=count+1
    print(count)
n=input("Enter a String : ")
str(n)

 