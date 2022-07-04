userInput = input("Pattern: ")
print("3rd=", userInput[3], "length=", len(userInput))
for index, value in enumerate(userInput):
    if value == " ":
        print("l5", index)
        userChar = "userChar"
    # A for capital A
    elif value == "A":
        print("Use capital letters")
        userA = "userA"
# a for small letters
    elif value == "a":
        print("Use small letters")
        usera = "usera"
# 1 for digits
    elif value == "1":
        print("Use digits")
        user1 = "user1"
    for char in value:
        # print("charVal",char)
        pass

# now how to mix this mess ?
