# Enter Key
from unittest import result


key = input("Enter key: ")
key = key.replace(" ", "")
key = key.upper()

# Create a matrix 5 x 5


def matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]


result = list()

# Storing key
for letters in key:
    if letters not in result:
        if letters == "J":
            result.append("I")
        else:
            result.append(letters)

index = 0

# Storing other character A=65...Z=90
for i in range(65, 91):
    if chr(i) not in result:
        if i == 73 and chr(74) not in result:
            result.append("I")
            index = 1
        elif index == 0 and i == 73 or i == 74:
            pass
        else:
            result.append(chr(i))

# Initialize the matrix
m = 0
myMatrix = matrix(5, 5, 0)
# Making matrix
for i in range(0, 5):
    for j in range(0, 5):
        myMatrix[i][j] = result[m]
        m += 1

# get location for each characters


def locChar(letters):
    loc = list()
    if letters == "J":
        letters = "I"
    for i, j in enumerate(myMatrix):
        for k, l in enumerate(j):
            if letters == l:
                loc.append(i)
                loc.append(k)
                return loc

# Encryption


def encrypt():
    plaintext = str(input("Enter your plaintext: "))
