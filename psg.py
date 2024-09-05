#Password Generator
import random

generate = input("Hello, do you wish to generate a password? ")

def GeneratePassword():

    contains = input("What do you want your password to consist of (digits/characters/symbols)?: ")

        # Allowing user to change length of password
    length = input("How long should the password be: ")

        # Declaring list of characters, digits to be used in password
    if contains.lower() == "digits":
            pass1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if contains.lower() == "characters":
            pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D']
    if contains.lower() == "symbols":
           pass1 = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    if contains.lower() == "":
          print("Please enter a data type!")

    password = ""

        # Generating password
    for x in range(int(length)):
         password = password + random.choice(pass1)[0]

        #Displaying password to user
    print("Your new password is\n: ", password)


if generate.lower() == 'yes':
    GeneratePassword()
else:
    print("Have a wonderful and blessed day!!")
