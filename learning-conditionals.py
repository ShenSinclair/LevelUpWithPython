name = input("What is your name? ")

if len(name) >= 6:
    print("Your name is too long")
elif len(name) == 5:
    print("Your name is 5 characters")
elif len(name) >= 4:
    print("Your name is 4 characters or more")
else:
    print("Your name is short.")