books = [
    {"title": "Python Basics", "author": "John Smith", "available": True},
    {"title": "Data Science", "author": "Jane Doe", "available": True},
    {"title": "Clean Code", "author": "Robert Martin", "available": False},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "available": True},
    {"title": "Deep Learning", "author": "Ian Goodfellow", "available": True},
]


def search_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    raise ValueError(f"Book '{title}' not found.")


def borrow_book(title):
    book = search_book(title)
    if not book["available"]:
        raise ValueError(f"'{title}' is already borrowed.")
    book["available"] = False
    return book


def return_book(title):
    book = search_book(title)
    if book["available"]:
        raise ValueError(f"'{title}' was not borrowed.")
    book["available"] = True
    return book


def show_available():
    print("\n--- Available Books ---")
    for book in books:
        if book["available"]:
            print(f"{book['title']} by {book['author']}")


def main():
    while True:
        action = input("\nAction (borrow/return/list/quit): ").strip().lower()
        if action == "quit":
            break
        if action == "list":
            show_available()
            continue
        title = input("Enter book title: ").strip()
        try:
            if action == "borrow":
                book = borrow_book(title)
                print(f"Borrowed '{book['title']}'.")
            elif action == "return":
                book = return_book(title)
                print(f"Returned '{book['title']}'.")
            else:
                print("Unknown action.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()