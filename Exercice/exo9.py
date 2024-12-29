cities = []

while True:
    city = input("Enter city name (type 'stop' to end): ")
    if city == "stop":
        break
    population = len(city) * 1000000
    cities.append((city, population))

cities.sort(key=lambda x: x[1], reverse=True)

for city, population in cities:
    print(f"{city}: {population}")
