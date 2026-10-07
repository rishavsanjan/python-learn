import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

while True:
    characterGroups = [lowercase, uppercase, numbers]
    generatedPassword = ""

    try:
        passwordLength = int(input("Enter password length that you want : "))
    except ValueError:
        print("Invalid Input!")
        continue

    if passwordLength < 3:
        print("Password length must be at least 3.")
        continue

    break


generatedPassword += random.choice(lowercase)
generatedPassword += random.choice(uppercase)
generatedPassword += random.choice(numbers)
for x in range(0,passwordLength - 3):
    randomGroup = random.choice(characterGroups)
    generatedPassword += random.choice(randomGroup)



print(generatedPassword)

l = list(generatedPassword)

random.shuffle(l)
finalPassword = "".join(l)
print(finalPassword)

