with open (r"C:\Users\shree\OneDrive\Pictures\Screenshots\Screenshot 2025-04-28 205147.png","rb") as file:
    rawdata = file.read()

with open ("img.png","wb") as file:
    file.write(rawdata)