menu = {
    "burger": 5.0,
    "pizza": 8.5,
    "pasta": 7.0,
    "salad": 4.0,
    "steak": 12.0,
    "fries": 3.0,
    "soup": 3.5,
    "soda": 1.5,
}

TAX_RATE = 0.10
order = []


def display_menu():
    print("\n--- Menu ---")
    for item, price in menu.items():
        print(f"{item:<10} {price:.2f}")


def add_item(name, qty):
    if name not in menu:
        raise ValueError(f"'{name}' is not on the menu.")
    if qty <= 0:
        raise ValueError("Quantity must be greater than zero.")
    order.append({"name": name, "qty": qty, "price": menu[name]})


def calculate_bill():
    subtotal = sum(entry["qty"] * entry["price"] for entry in order)
    tax = subtotal * TAX_RATE
    return subtotal, tax, subtotal + tax


def display_order():
    print("\n--- Order ---")
    for entry in order:
        line = entry["qty"] * entry["price"]
        print(f"{entry['name']:<10} x{entry['qty']:<3} = {line:.2f}")
    subtotal, tax, total = calculate_bill()
    print(f"\nSubtotal : {subtotal:.2f}")
    print(f"Tax(10%) : {tax:.2f}")
    print(f"Total    : {total:.2f}")


def main():
    display_menu()
    while True:
        name = input("\nEnter food item (or 'done'): ").strip().lower()
        if name == "done":
            break
        try:
            qty = int(input("Enter quantity: "))
            add_item(name, qty)
            print(f"Added {qty} x {name}.")
        except ValueError as error:
            print(f"Error: {error}")
    if order:
        display_order()
    else:
        print("No items ordered.")


if __name__ == "__main__":
    main()