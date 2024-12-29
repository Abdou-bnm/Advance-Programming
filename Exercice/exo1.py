name = input("Please enter your name: ")

if name == "VIP":
    print("Enjoy the show for free!")
else:
    ticket_price = 15.50
    tickets = int(input("How many tickets would you like to buy? "))
    total_cost = tickets * ticket_price
    print(f"The total cost is {total_cost}")
    print("Enjoy your tickets!")
