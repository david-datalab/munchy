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

# from random import *
dic = {}


def main():
    user_input = input("input:")
    for index, value in enumerate(user_input):
        # print(index, value)
        if value == " ":
            pass
        if value == "1":
            for i in string.digits:
                # print(index, i)
                dic[index] = string.digits
                # print(dic)
        elif value == "A":
            for i in string.ascii_uppercase:
                # print(index, i)
                dic[index] = string.ascii_uppercase
        elif value == "a":
            for i in string.ascii_lowercase:
                # print(index, i)
                dic[index] = string.ascii_lowercase
        elif value == "*":
            # print(index, string.punctuation)
            dic[index] = string.punctuation
        else:
            value = None
            print("None")
            pass

    return dic


if __name__ == "__main__":
    main()
    # print(dic)
    for i in dic.values():
        for x in i:
            print(x)
