word = input("Word: ")
padding = (30 - len(word)) // 2

print("*" * 30)
print("*" + " " * padding + word + " " * (30 - len(word) - padding) + "*")
print("*" * 30)
