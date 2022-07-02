
"""
a program to help remember or recover forgotten passwords
how to determine how will it work ?
what a password consist of ?
all characters and patterns
1 enter length
2 what does it include? A a 1 *
3 pattern
4 what about other languages ?
5 passwords are hashed why not make a database to save plane passwords and their hashes at the same time incase we need
to look for a hashed password
6 should I make it serial instead of random ?
7 need to make sure passwords aren't repeated
"""
import string
from random import *

print("""
Welcome to Munchy, a smart password recovery utility.
1. To start enter the length or the range of your password
2. if you remember a pattern you can enter it also
3. you can choose if the password consist of only letters or digits or special characters
4. you can choose a name for the output list
""")

# user inputs | add choice for only letters or digits or special characters
guess = int(input("How many passwords to generate? "))  # will be deprecated when a database will be added
length = int(input("Enter Length: "))
pattern = input("Enter Pattern: ")
for char in pattern:
    if char == "A":
        print("A")
    elif char == "a":
        print("a")
    elif char == "1":
        print("a")
    elif char == "*":
        print("*")
    else:
        print("error")
        break
# characters variables
strings = string.ascii_letters
digits = string.digits
specChars = string.punctuation

# user selections for generating passwords
characters = strings + digits + specChars

# the results
for i in range(guess):
    password = "".join(choice(characters) for x in range(length))
    print(password)