# PartD:real-life Scenario
# 6.Create a small bill calculator:
item_name = input("Enter the Item Name:- ")
quantity = int(input("Enter the Item Quantity:- "))
price_per_item = float(input("Enter the price per item:- "))
total_cost = quantity * price_per_item

print("\n*****Bill Summary*****")
print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"price per item: {price_per_item} rs")
print(f"Total Cost: {total_cost} rs")
