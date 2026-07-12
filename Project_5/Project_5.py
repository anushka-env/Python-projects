# Library managment system

books = {
    "Python Basics": 3,
    "Java Programming": 2,
    "Data Structures": 4,
    "Machine Learning": 1
}

borrowed_books = []


def view_books():
    print("\n========== AVAILABLE BOOKS ==========\n")

    for key in books:
        print(key, ":", books[key])

    print("\n=====================================\n")


def borrow_book():
    print("\n========== BORROW BOOK ==========\n")

    book_name = input("Enter book name: ")

    if book_name in books:
        if books[book_name] > 0:
            books[book_name] -= 1
            borrowed_books.append(book_name)

            print("\nBook borrowed successfully.\n")

            with open("books.txt", "a") as f:
                f.write("Borrowed book: " + book_name + "\n")

        else:
            print("\nBook is currently unavailable.\n")

    else:
        print("\nBook not found.\n")


def return_book():

    print("\n========== RETURN BOOK ==========\n")

    if not borrowed_books:
        print("\nNo books borrowed yet.\n")

    else:
        book_name = input("Enter book name: ")

        if book_name in borrowed_books:
            borrowed_books.remove(book_name)
            books[book_name] += 1

            print("\nBook returned successfully.\n")

            with open("books.txt", "a") as f:
                f.write("Returned book: " + book_name + "\n")

        else:
            print("\nYou have not borrowed this book.\n")


def my_borrowed_books():

    print("\n========== MY BORROWED BOOKS ==========\n")

    if not borrowed_books:
        print("No books borrowed.\n")

    else:
        for i in borrowed_books:
            print(i)

        print()


def add_book():

    print("\n========== ADD BOOK ==========\n")

    num = int(input("Enter how many books you want to add: "))

    for i in range(num):

        print(f"\nBook {i + 1}\n")

        new_book = input("Enter book name: ")
        new_book_qty = int(input("Enter quantity: "))

        if new_book in books:
            books[new_book] += new_book_qty
        else:
            books[new_book] = new_book_qty

        print("\nBook(s) added successfully.\n")

        with open("books.txt", "a") as f:
            f.write(
                f"Added book: {new_book} Quantity: {new_book_qty}\n"
            )


def main():

    while True:

        print("\n===================================")
        print("      LIBRARY MANAGEMENT SYSTEM")
        print("===================================")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. My Borrowed Books")
        print("5. Add Book")
        print("6. Exit")
        print("===================================")

        try:
            choice = int(input("Enter Your Choice: "))

            print()

            if choice == 1:
                view_books()

            elif choice == 2:
                borrow_book()

            elif choice == 3:
                return_book()

            elif choice == 4:
                my_borrowed_books()

            elif choice == 5:
                add_book()

            elif choice == 6:
                print("\nThank You For Visiting... Keep Learning!\n")
                break

            else:
                print("\nInvalid Choice!\n")

        except ValueError:
            print("\nPlease Enter Numbers Only!\n")


main()