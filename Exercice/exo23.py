try:
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Please enter a positive number.")
    else:
        for i in range(-n, n + 1):
            if i != 0:
                print(i)
except ValueError:
    print("Invalid input. Please enter an integer.")
