# This program asks the user to input any positive integer and
# outputs

x = int(input("Enter an integer:"))

if x % 2 == 0:
    y = x / 2
    if y != 1:
        print(int(y))