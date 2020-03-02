# This program calculates your Body Mass Index (BMI) 
# based on your height and weight, in metres squared.

height = float(input("Enter your height (in cm): "))
weight = float (input("Enter your weight (in kg): "))

# Requesting user to input their height in cm and their weight in kg.
# This program allows for decimals.

bmi = weight / ((height / 100) ** 2)
# Formula for calculating BMI (allowing for cm input to be converted to metres).

print("Your body mass index is", bmi, "in metres squared.")
# Prints result.


