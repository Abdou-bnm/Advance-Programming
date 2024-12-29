amount = float(input("Total amount: "))
items = int(input("Number of items: "))
day = input("Day of the week: ")

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    discount = 0.10
else:
    discount = 0.20

if items > 5:
    discount += 0.05

total_price = amount * (1 - discount)
print(f"Total price after discount: {total_price} dinars")
