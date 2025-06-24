# 9.Email Generator
# Function generate_email(name, domain="example.com")
# Input: "John Doe" → Output: "john.doe@example.com"
def generate_email(name,domain="example.com"):
    username = name.strip().lower().replace(" "," ")
    email = f"{username}@{domain}"
    return email

full_name = input("Enter your full name: ")
eamil = generate_email(full_name)
print(f"Generated email: {email}")
