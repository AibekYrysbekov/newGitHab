name = input("Enter a car brand: ").lower()
year = int(input("Enter year of a car: "))
probeg = int(input("Enter desired car mileage: "))
color = input("Enter the color of the car: ").lower()
rul = input("Select handlebar side: ").lower()
owners = int(input("Enter the number of owners: "))
price = int(input("Enter your desired price: "))

if name == "lexus" or name == "toyota" and year >= 2004 and probeg <= 150000:
    if color == "white" or color == "grey" and rul == "left" and owners <= 2 and price <= 10000:
        print("Мы нашли для вас машину")
    else:
        print("Ничего не найдено")
elif name == "lexus" or name == "toyota" and year >= 2004 and probeg <= 200000:
    if color == "white" or color == "grey" and rul == "left" and owners <= 2 and price <= 8000:
        print("Мы нашли для вас машину")
    else:
        print("Ничего не найдено")
else:
    print("Ничего не найдено")