string = input("Please type in a string: ")

for vowel in "aeo":
    if vowel in string:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
