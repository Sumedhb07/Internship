txt="Hello World Binary"
with open ("binary.bin","wb") as file:
    file.write(txt.encode())
    
with open ("Binary.bin","rb") as file:
   var = file.read()
   print(var.decode())