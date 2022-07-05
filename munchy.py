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
"""
guess = int(input("How many passwords to generate? "))  # will be deprecated when a database will be added
# length = int(input("Enter Length: "))
pattern = input("Enter Pattern: ")
for char in pattern:
    # print(char)
    if char == "A":
        # print("A")
        strings = string.ascii_letters
        if char == "a":
            # print("a")
            strings = string.ascii_letters
            if char == "1":
                # print("1")
                digits = string.digits
                if char == "*":
                    # print("*")
                    specChars = string.punctuation
                else:
                    print("error")
                    pass
"""
# for i in range(guess):
#    password = "".join(choice(strings + digits + specChars) for x in range(len(pattern)))
#    print(password)
print("Enter Pattern:")


def pattern_loader(userinput):
    userinput = userinput.split(' ')
    print(userinput)
    if "A" in userinput:
        print("yes A")
    elif "a" in userinput:
        print("yes a")
    elif "1" in userinput:
        print("yes 1")
    else:
        print("No")
    return None

pattern_loader(input())
# I need to split the pattern into a list and depending on the characters I will analyse each character to generate a password

