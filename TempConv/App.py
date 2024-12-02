
def convert_temperature(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)

    print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
    
    if celsius < 0:
        print("Brr! It's cold in here!")


if __name__ == "__main__":
    
    while True:
        try:
            fahrenheit = float(input("Please type in a temperature (F): "))
            convert_temperature(fahrenheit)
        except ValueError:
            print("Please enter a valid number!")
            
        if(input("Do you want to convert another temperature? (y/n) ") != "y"):
            print("Goodbye!")
            break
