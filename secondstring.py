#This program asks the user to input a string
#and outputs every second letter in reverse order.

sentence = input("Please enter a sentence:")

result = sentence[::-2]
# Outputs every second letter in reverse order. [::-1] would output
# the entire string in reverse order.

print(result)


