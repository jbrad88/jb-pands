# This program asks the user to input any positive integer and
# outputs the successive values of the following calculation:
# At each step, calculate the next value by taking the current value,
# and if it is even, divide it by two, but if it is odd, multiply it
# by three and add one. The program ends when the value reaches 1.

x = int(input("Enter an integer:"))

while x != 1:
    if x % 2 == 0:
       print(round(x, ndigits = None))
       x = x / 2
       
    else:
        print(round(x, ndigits = None))
        x = (x*3) + 1

print(round(x,ndigits=None))


