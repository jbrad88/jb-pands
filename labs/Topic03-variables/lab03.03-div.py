# Program that reads in two numbers and divides
# the first one by the second. Output gives the integer
# result and the remainder.

x = int(input('Enter first number:'))
y = int(input('Enter second number:'))

answer = int(x/y)
remainder = x%y

print(x, 'divided by', y, 'is', answer, 'with remainder', remainder, '.')


