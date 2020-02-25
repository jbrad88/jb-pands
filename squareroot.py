# Jody Bradley
# This programme take a postive floating-point number
# and outputs an approximation of its square root.

x = float(input('Enter a positive floating point number:'))

def sqrt(x):
    return x ** 0.5

ans = sqrt(x)

print('The square root of', x, 'is approximately', ans)
