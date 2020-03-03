e = 'e'
answer = 0

with open(r"C:\\Users\\jodyb\\Desktop\\jb-pands\\moby-dick.txt", "r") as f:
# I was getting a FileNotFoundError message for f = open('moby-dick', 'r')
# I found this alternative method on stackoverflow - see references below.
     for line in f:
         words = line.split()
# For loop reads through the lines of text in the file and splits each into a list of words.
         for i in words:
             for letter in i:
                 if(letter==e):
                     answer=answer+1

print(answer)


# REFERENCES
# https://stackoverflow.com/questions/20588840/unicode-error-opening-txt-files-with-python
# https://www.sanfoundry.com/python-program-read-file-counts-number/
