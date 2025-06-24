# file = open("notes.txt","a+") #file Create
# file.write("Hello World!! Welcome to Rich System")
# file.write("\n i'm Sumedh Badgujar i'm 18 years old ")
# print(file.tell())#check the pointer position
# file.seek(0) #set the pointer position as required 
# #print(file.readlines())
# #print(file.read())
# #file.close()

with open("notes.txt","w+") as file:
    file.write("Hello World!! Welcome to Rich System")
    file.write("\n i'm Sumedh Badgujar i'm 18 years old ")
    file.seek(0) #set the pointer position as required 
# count = 0
# #for i in file:
#     count+=1
#     print(count)
    # file1 = file.read()
    # var1 = file1.readlines()
    count=0
    for i in file:
        count+=1
    print("Total number of line in File:",(count))
    file.seek(0)
    r=file.read()
    demo=r.split()
    print("Total number of word in file:",len(demo))
    print("Total number of character in file: ",len(r))
    




