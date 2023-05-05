shopping_cart = {}
cost = 0

while True:
    item = input("\nPlease enter the desired item: ")
    price = float(input("Enter the price of the desired item: "))
    shopping_cart[item] = price
    cost += price
    print(item, "was added to your shopping cart.")
    transactmore = input("\nDo you wish to buy another item? yes/no: ")
    if transactmore.lower() != "yes":
        break

print("Thank you! Please shop again next time. Your total is ₱",cost)