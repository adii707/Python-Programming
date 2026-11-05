
# Library Book Borrowing System

# Dictionary to store book details
books = {
    101: "Python Programming",
    102: "Data Structures",
    103: "Database Management",
    104: "Computer Networks",
    105: "Artificial Intelligence"
}

# Set of available book IDs
available_books = set(books.keys())

# Set of borrowed book IDs
borrowed_books = set()

# List to store borrowing records as tuples
records = []

# Dictionary to store borrow counts per student
borrow_count = {}

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display Borrowing Records")
    print("5. Display Borrow Counts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nAvailable Books:")
        for book_id in available_books:
            print(book_id, "-", books[book_id])

        print("\nBorrowed Books:")
        for book_id in borrowed_books:
            print(book_id, "-", books[book_id])

    elif choice == 2:
        student_id = input("Enter Student ID: ")
        book_id = int(input("Enter Book ID: "))

        if book_id not in books:
            print("Book does not exist!")

        elif book_id not in available_books:
            print("Book is currently unavailable!")

        else:
            available_books.remove(book_id)
            borrowed_books.add(book_id)

            records.append((student_id, book_id, "Borrowed"))

            borrow_count[student_id] = borrow_count.get(student_id, 0) + 1

            print("Book borrowed successfully!")

    elif choice == 3:
        student_id = input("Enter Student ID: ")
        book_id = int(input("Enter Book ID: "))

        if book_id not in borrowed_books:
            print("This book is not currently borrowed!")

        else:
            borrowed_books.remove(book_id)
            available_books.add(book_id)

            records.append((student_id, book_id, "Returned"))

            print("Book returned successfully!")

    elif choice == 4:
        print("\nBorrowing Records:")
        for record in records:
            print(record)

    elif choice == 5:
        print("\nBorrow Counts Per Student:")
        for student, count in borrow_count.items():
            print(student, ":", count)

    elif choice == 6:
        print("Thank you for using the Library System!")
        break

    else:
        print("Invalid choice! Please try again.")
