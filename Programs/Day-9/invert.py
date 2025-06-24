#invert the values in Dictionary
my_dic={'a':1,'b':2,'c':1}
dic1={}
for key,value in my_dic.items():
    if value in dic1:
        dic1[value].append(key)
    else:
        dic1[value]=[key]
print(dic1)


#{1:['a','c'],2:'b}