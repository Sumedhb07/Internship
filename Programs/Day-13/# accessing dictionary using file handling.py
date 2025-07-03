# accessing dictionary using file handling 
dict1 = {"apple" : 10 , "banana": 20}
try : 
    fruit = input("Enter the name of fruit : ")
    file_name = input("Enter the name of file  : ")
    
    print(f"the name of fruit is {fruit} and price is {dict1[fruit]}")
    file = open(file_name,"r")
  
except ( KeyError , FileNotFoundError ) as e :
    print(e)
    