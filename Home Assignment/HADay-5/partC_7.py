#7.Use a for loop to print numbers from 1 to 10, but skip printing 5.
for i in range(1,11):
    if i == 5:
        continue
    print(i)