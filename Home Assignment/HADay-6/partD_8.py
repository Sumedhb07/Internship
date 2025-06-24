# Part D: Data Formatting + Return
# 8.Currency Converter
# Function convert_to_usd(inr, rate=83.2) → converts INR to USD (default rate 83.2)
def convert_to_usd(inr, rate= 83.2):
    usd = inr / rate
    return round(usd, 2)
inr_amount = float(input("Enter amount in INR: "))
usd_amount = convert_to_usd(inr_amount)
print(f"{inr_amount} INR is approximately {usd_amount} USD")