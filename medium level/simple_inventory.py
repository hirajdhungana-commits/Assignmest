inventory = {
    "apple": 20,
    "banana": 15,
    "mango": 10,
    "orange": 8
}

item = input("Enter item name: ").lower()

if item in inventory:
    sold = int(input("How many items were sold? "))

    inventory[item] -= sold

    if inventory[item] == 0:
        del inventory[item]

    print("Updated inventory:")
    print(inventory)

else:
    print("Item not found in inventory.")