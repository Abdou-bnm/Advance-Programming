numbers = [1, 2, 3, 4, 5]

while True:
    print("\nMenu:")
    print("1. Append")
    print("2. Insert")
    print("3. Pop")
    print("4. Remove")
    print("5. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        value = int(input("Enter value: "))
        numbers.append(value)
    elif choice == "2":
        value = int(input("Enter value: "))
        index = int(input("Enter index: "))
        if 0 <= index <= len(numbers):
            numbers.insert(index, value)
        else:
            print("Invalid index!")
    elif choice == "3":
        if numbers:
            numbers.pop()
        else:
            print("List is empty!")
    elif choice == "4":
        value = int(input("Enter value to remove: "))
        if value in numbers:
            numbers.remove(value)
        else:
            print("Value not found!")
    elif choice == "5":
        break
    else:
        print("Invalid choice!")

    print("Updated List:", numbers)
