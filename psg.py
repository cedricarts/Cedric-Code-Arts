#Password Generator
import random

# Allowing user to change length of password
length = input("How long should the password be: ")

# Declaring list of characters, digits to be used in password
pass1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

password = ""

# Generating password
for x in range(int(length)):
    password = password + random.choice(pass1)[0]

#Displaying password to user
print("Your new password is\n: ", password)
    