# Enter Key
from email import message
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
    message = str(input("Enter your message: "))
    message = message.upper()
    message = message.replace(" ", " ")
    i = 0
    for s in range(0, len(message) + 1, 2):
        if s < len(message) - 1:
            if message[s] == message[s + 1]:
                message = message[:s + 1] + "X" + message[s + 1]
    if len(message) % 2 != 0:
        message = message[:] + "X"
    print("Cipher text:", end=" ")
    while i < len(message):
        loc = list()
        loc = locChar(message[i])
        loc1 = list()
        loc1 = locChar(message[i + 1])
        if loc[1] == loc1[1]:
            print("{}{}".format(
                myMatrix[(loc[0]+1) % 5][loc[1]], myMatrix[(loc1[0]+1) % 5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(
                myMatrix[loc[0]][(loc[1]+1) % 5], myMatrix[loc1[0]][(loc1[1]+1) % 5]), end=' ')
        else:
            print("{}{}".format(
                myMatrix[loc[0]][loc1[1]], myMatrix[loc1[0]][loc[1]]), end=' ')
        i = i+2

# decryption


def decrypt():
    message = str(input("Enter Cipher text:"))
    message = message.upper()
    message = message.replace(" ", "")
    print("plain text:", end=' ')
    i = 0
    while i < len(message):
        loc = list()
        loc = locChar(message[i])
        loc1 = list()
        loc1 = locChar(message[i+1])
        if loc[1] == loc1[1]:
            print("{}{}".format(
                myMatrix[(loc[0]-1) % 5][loc[1]], myMatrix[(loc1[0]-1) % 5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(
                myMatrix[loc[0]][(loc[1]-1) % 5], myMatrix[loc1[0]][(loc1[1]-1) % 5]), end=' ')
        else:
            print("{}{}".format(
                myMatrix[loc[0]][loc1[1]], myMatrix[loc1[0]][loc[1]]), end=' ')
        i = i+2


while(1):
    choice = int(input("\n 1.Encryption \n 2.Decryption: \n 3.Exit"))
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    elif choice == 3:
        exit()
    else:
        print("Choose correct choice")
