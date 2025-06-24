# 10.Password Masker
# Function mask_password(password) returns a masked version
# Example: "secret" → "******"
def mask_password(password):
    return '*' * len(password)
pwd = input("Enter your password: ")
masked = mask_password(pwd)
print(f"Masked password: {masked}")