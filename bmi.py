# This program calculates your Body Mass Index (BMI) 
# based on your height and weight, in metres squared.

height = float(input("Enter your height (in cm): "))
weight = float (input("Enter your weight (in kg): "))

bmi = weight / ((height / 100) ** 2)

print("Your body mass index is", bmi, "in metres squared.")


