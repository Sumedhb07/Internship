#Find the Repeated Number from Tuple
my_tuple = (2,3,4,5,6,7,4,5,3,2,5)
repeated = []
count=0
for i in my_tuple:
    if my_tuple.count(i) > 1 and i not in repeated:
        repeated.append(i)     
        count = count + 1
print(f"count is :- {count}")  
print(f"Repeated number:- {repeated}")
        


