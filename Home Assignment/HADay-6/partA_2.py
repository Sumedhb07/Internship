# 2.BMI Calculator
# Define a function calculate_bmi(weight, height) that:
# oTakes weight in kg and height in meters
# oCalculates BMI: bmi = weight / (height ** 2)
# oReturns BMI and category:
# <18.5: Underweight
# 18.5–24.9: Normal
# 25–29.9: Overweight
# 30+: Obese
def calculate_bmi(weight , height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category
    
weight = float(input("Enter your weight in KG:- "))
height = float(input("Enter your height in meter:- "))

bmi_value, bmi_category = calculate_bmi(weight , height) 

print(f"your bmi is: {bmi_value:.2f}")
print(f"Category: {bmi_category}")