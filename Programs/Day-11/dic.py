prices = {"apple":10,"banana":5}
try:
    fruit = input("Enter a Fruit Name:")
    price = prices[fruit]
    file = input("Enter a File Name: ")
    print("The Price is: ",prices[fruit])
    with open(file,"r") as file: 
        content = file.read()
        print("content:",content)
    
        
except(KeyError,FileNotFoundError) as e:
    print("Key Not Found",e)
    print("File Not Found",e)


