import string
import random
length = int(input("enter the number of characters in password:"))
print('''Select a type of password
        1. Character
        2. Number
        3. Special Characters
        4. Exit''')
characterList = ""
while(True):
    choice = int(input("Pick a Number:"))
    if choice == 1:
        characterList += string.ascii_letters #For simple character password generation
    elif (choice == 2):
        characterList += string.digits # For Number password generation/ digits
    elif (choice == 3):
        characterList += string.punctuation #for special characters
    elif(choice == 4):
        break
    else:
        print("Pick a valid number!")
password = []
for i in range(length):
    randomChoice = random.choice(characterList)
    password.append(randomChoice)
print("The Random Password is:"+"".join(password))