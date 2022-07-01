
"""
a program to help remember or restore forgotten passwords
how to determine how will it work ?
what a password consist of ?
all characters and patterns
1 enter length
2 what does it include? A a 1 *
3 pattern
4 what about other languages ?
5 passwords are hashed why not make a database to save plane passwords and their hashes at the same time incase we need
to look for a hashed password
"""
import string
from random import *
# user inputs | add choice for only letters or digits or special characters
guess = int(input("How many passwords to generate? "))  # will be deprecated when a database will be added
length = int(input("Enter Length: "))
pattern = input("Enter Pattern: ")
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
