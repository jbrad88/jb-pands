# This program reads in a string and strips any leading
# or trailing spaces. It also converts all the letters to
# lower case. This program also outputs the length of the original
# string and the normalised one.

#raw string
x = input('Please enter a string:')

#normalised string
y = x.strip().lower()

#length of rawstring
a = len(x)

#length of normalised string
b = len(y)

print('That string normalised is', y)
print('We reduced the input string from', a, 'to', b, 'characters.')