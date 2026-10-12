products = {
    "apple": {"price": 1.5, "quantity": 10},
    "banana": {"price": 0.8, "quantity": 20},
    "milk": {"price": 2.5, "quantity": 5},
    "bread": {"price": 3.0, "quantity": 8},
    "eggs": {"price": 4.5, "quantity": 12},
    "cheese": {"price": 6.0, "quantity": 3},
}

cart = {}


def add_to_cart(name, qty):
    if name not in products:
        raise ValueError(f"Product '{name}' does not exist.")
    available = products[name]["quantity"]
    if qty <= 0:
        raise ValueError("Quantity must be greater than zero.")
    if qty > available:
        raise ValueError(f"Only {available} of '{name}' available.")

    products[name]["quantity"] -= qty
    cart[name] = cart.get(name, 0) + qty


def calculate_total():
    total = 0.0
    for name, qty in cart.items():
        total += products[name]["price"] * qty
    return total


def display_cart():
    print("\n--- Cart ---")
    if not cart:
        print("Cart is empty.")
        return
    for name, qty in cart.items():
        total += products[name]["price"] * qty
    return total


def display_cart():
    print("\n--- Cart ---")
    if not cart:
        print("Cart is empty.")
        return
    for name, qty in cart.items():
        price = products[name]["price"]
        print(f"{name:<10} x{qty:<3} @ {price:.2f} = {price * qty:.2f}")


def main():
    while True:
        name = input("\nEnter product name (or 'done'): ").strip().lower()
        if name == "done":
            break
        try:
            qty = int(input("Enter quantity: "))
            add_to_cart(name, qty)
            print(f"Added {qty} x {name}.")
        except ValueError as error:
            print(f"Error: {error}")

    display_cart()
    print(f"\nTotal bill: {calculate_total():.2f}")


if __name__ == "_main_":
    main()