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
print("Enter Pattern:")
lst = list()


def pattern_loader(userinput):
    for singleChar in userinput:
        if singleChar == "A" or singleChar == "a" or singleChar == "1" or singleChar == "*" or singleChar == " ":
            lst.append(singleChar)
        else:
            print("not a valid pattern")
            break
    return lst


pattern_loader(input())
number_of_passwords = int(input("How many passwords to generate? "))
for i in range(number_of_passwords):
    if "A" and "a" and "1" and "*" in lst:
        password = "".join(choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for x in range(len(lst)))
        print(password)
    elif "A" and "a" in lst:
        password = "".join(choice(string.ascii_uppercase + string.ascii_lowercase) for x in range(len(lst)))
        print(password)
    elif "A" and "1" in lst:
        password = "".join(choice(string.ascii_uppercase + string.digits) for x in range(len(lst)))
        print(password)
    elif "A" and "*" in lst:
        password = "".join(choice(string.ascii_uppercase + string.punctuation) for x in range(len(lst)))
        print(password)
    elif "1" and "a" in lst:
        password = "".join(choice(string.digits + string.ascii_lowercase) for x in range(len(lst)))
        print(password)
    elif "*" and "a" in lst:
        password = "".join(choice(string.punctuation + string.ascii_lowercase) for x in range(len(lst)))
        print(password)
    elif "1" and "*" in lst:
        password = "".join(choice(string.digits + string.punctuation) for x in range(len(lst)))
        print(password)
    elif "A" in lst:
        password = "".join(choice(string.ascii_uppercase) for x in range(len(lst)))
        print(password)
    elif "a" in lst:
        password = "".join(choice(string.ascii_lowercase) for x in range(len(lst)))
        print(password)
    elif "1" in lst:
        password = "".join(choice(string.digits) for x in range(len(lst)))
        print(password)
    elif "*" in lst:
        password = "".join(choice(string.punctuation) for x in range(len(lst)))
        print(password)
    else:
        print("invalid pattern")
# To fight randomness or not ???


"""
  # will be deprecated when a database will be added
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
#