cart = ["apple", "milk", "bread", "apple", "eggs", "milk"]
cart = list(set(cart))

cart.append("cheese")

cart.remove("bread")

cart.sort()
print("Final cart:",cart)
print("Number of different items:",len(cart))