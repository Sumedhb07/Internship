# 7.A shop gives discount:
# o	Total bill < 500 → No discount
# o	500 to 1000 → 5% discount
# o	Above 1000 → 10% discount
# Ask the user to enter the total bill amount
bill_amount = float(input("Enter the total bill amount: "))

# Determine the discount
if bill_amount < 500:
    discount = 0
elif 500 <= bill_amount <= 1000:
    discount = 0.05 * bill_amount  # 5% discount
else:
    discount = 0.10 * bill_amount  # 10% discount

# Calculate the final amount after discount
final_amount = bill_amount - discount

# Display the final amount
print(f"Discount applied: {discount:.2f}")
print(f"Final bill amount: {final_amount:.2f}")
