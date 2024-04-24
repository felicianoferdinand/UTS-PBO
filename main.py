from book import Book
from member import Member
from library import Library

def main():
    library = Library()

    default_books = [
        Book("B001", "Python Programming", "Michael Smith", 5),
        Book("B002", "Data Structures and Algorithms", "Alice Brown", 3),
        Book("B003", "Machine Learning Basics", "John Johnson", 7)
    ]
    for book in default_books:
        library.add_book(book)
    
    default_members = [
        Member("M001", "Budi", "budi@gmail.com"),
        Member("M002", "Joko", "joko@gmail.com"),
        Member("M003", "Agus", "agus@gmail.com")
    ]
    for member in default_members:
        library.add_member(member)

    print("Welcome to UKRIDA E-Library")
    while True:
        print("\nMenu:")
        print("1. Add a new book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. Search for books")
        print("5. Show all books")
        print("6. Add a new member")
        print("7. Update a member")
        print("8. Delete a member")
        print("9. Show all members")
        print("10. Checkout a book")
        print("11. Return a book")
        print("12. Show borrowing records")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_book(library)
        elif choice == '2':
            update_book(library)
        elif choice == '3':
            delete_book(library)
        elif choice == '4':
            search_books(library)
        elif choice == '5':
            show_all_books(library)
        elif choice == '6':
            add_member(library)
        elif choice == '7':
            update_member(library)
        elif choice == '8':
            delete_member(library)
        elif choice == '9':
            show_all_members(library)
        elif choice == '10':
            checkout_book(library)
        elif choice == '11':
            return_book(library)
        elif choice == '12':
            show_borrowing_records(library)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")


def add_new_book(library):
    print("\nAdding a new book:")
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    copies_available = input("Enter number of copies available: ")

    # Validate input
    if not book_id or not title or not author or not copies_available:
        print("All fields are required.")
        return
    
    if not copies_available.isdigit():
        print("Number of copies must be a positive integer.")
        return
    
    copies_available = int(copies_available)

    # Check if book ID already exists
    for book in library.books:
        if book.get_book_id() == book_id:
            print("Book with this ID already exists.")
            return

    new_book = Book(book_id, title, author, copies_available)
    library.add_book(new_book)
    print("Book added successfully.")


def show_all_books(library):
    print("\nAll Books:")
    print("+" + ("-" * 97) + "+")
    print("| {:<10} | {:<40} | {:<20} | {:<15} |".format("Book ID", "Title", "Author", "Copies Available"))
    print("+" + ("-" * 97) + "+")
    for book in library.books:
        print("| {:<10} | {:<40} | {:<20} | {:<16} |".format(book.get_book_id(), book.get_title(), book.get_author(), book.get_copies_available()))
    print("+" + ("-" * 97) + "+")


def update_book(library):
    print("\nUpdating a book:")
    book_id = input("Enter book ID to update: ")

    # Check if book exists
    found_book = None
    for book in library.books:
        if book.get_book_id() == book_id:
            found_book = book
            break
    if not found_book:
        print("Book not found.")
        return

    title = input("Enter new title (leave blank to keep current): ")
    author = input("Enter new author (leave blank to keep current): ")
    copies_available = input("Enter new number of copies available (leave blank to keep current): ")

    if copies_available and not copies_available.isdigit():
        print("Number of copies must be a positive integer.")
        return

    if title:
        found_book.set_title(title)
    if author:
        found_book.set_author(author)
    if copies_available:
        found_book.set_copies_available(int(copies_available))

    print("Book updated successfully.")


def delete_book(library):
    print("\nDeleting a book:")
    book_id = input("Enter book ID to delete: ")

    # Check if book has been borrowed
    for member_id, books in library.borrow_records.items():
        if book_id in books:
            print("Book has been borrowed. Please return all borrowed copies before deleting the book.")
            return

    # Check if book exists
    found_book = None
    for book in library.books:
        if book.get_book_id() == book_id:
            found_book = book
            break
    if not found_book:
        print("Book not found.")
        return

    library.delete_book(book_id)
    print("Book deleted successfully.")


def search_books(library):
    print("\nSearching for books:")
    keyword = input("Enter title or author keyword: ")
    found_books = library.search_books(keyword)
    if not found_books:
        print("No books found.")
    else:
        print("Found Books:")
        for book in found_books:
            print(f"ID: {book.get_book_id()}, Title: {book.get_title()}, Author: {book.get_author()}, "
                  f"Copies Available: {book.get_copies_available()}")


def add_member(library):
    print("\nAdding a new member:")
    member_id = input("Enter member ID: ")
    name = input("Enter name: ")
    email = input("Enter email: ")

    # Validate input
    if not member_id or not name or not email:
        print("All fields are required.")
        return

    # Check if member ID already exists
    for member in library.members:
        if member.get_member_id() == member_id:
            print("Member with this ID already exists.")
            return

    new_member = Member(member_id, name, email)
    library.add_member(new_member)
    print("Member added successfully.")


def show_all_members(library):
    print("\nAll Members:")
    print("+" + ("-" * 68) + "+")
    print("| {:<10} | {:<20} | {:<30} |".format("Member ID", "Name", "Email"))
    print("+" + ("-" * 68) + "+")
    for member in library.members:
        print("| {:<10} | {:<20} | {:<30} |".format(member.get_member_id(), member.get_name(), member.get_email()))
    print("+" + ("-" * 68) + "+")


def update_member(library):
    print("\nUpdating a member:")
    member_id = input("Enter member ID to update: ")

    # Check if member exists
    found_member = None
    for member in library.members:
        if member.get_member_id() == member_id:
            found_member = member
            break
    if not found_member:
        print("Member not found.")
        return

    name = input("Enter new name (leave blank to keep current): ")
    email = input("Enter new email (leave blank to keep current): ")

    if name:
        found_member.set_name(name)
    if email:
        found_member.set_email(email)

    print("Member updated successfully.")


def delete_member(library):
    print("\nDeleting a member:")
    member_id = input("Enter member ID to delete: ")

    # Check if member has borrowed books
    if member_id in library.borrow_records:
        print("Member has borrowed books. Please return all borrowed books before deleting the member.")
        return

    # Check if member exists
    found_member = None
    for member in library.members:
        if member.get_member_id() == member_id:
            found_member = member
            break
    if not found_member:
        print("Member not found.")
        return

    library.delete_member(member_id)
    print("Member deleted successfully.")


def checkout_book(library):
    print("\nChecking out a book:")
    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")

    if not member_id or not book_id:
        print("Member ID and book ID are required.")
        return

    if library.borrow_book(member_id, book_id):
        print("Book checked out successfully.")
    else:
        print("Failed to check out book. Book not available or member not found.")


def return_book(library):
    print("\nReturning a book:")
    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")

    if not member_id or not book_id:
        print("Member ID and book ID are required.")
        return
    
    if library.return_book(member_id, book_id):
        print("Book returned successfully.")
    else:
        print("Failed to return book. Member has not borrowed this book.")


def show_borrowing_records(library):
    print("\nBorrowing Records:")
    print("+" + ("-" * 101) + "+")
    print("| {:<10} | {:<20} | {:<40} | {:<20} |".format("Member ID", "Member Name", "Book Title (ID)", "Date Borrowed"))
    print("+" + ("-" * 101) + "+")
    for member_id, books in library.borrow_records.items():
        member_name = [member.get_name() for member in library.members if member.get_member_id() == member_id][0]
        for book_id, book in books.items():
            print("| {:<10} | {:<20} | {:<40} | {:<20} |".format(
                member_id, 
                member_name, 
                book.get_title() + " (" + book_id + ")",
                book.get_date_borrowed().strftime("%Y-%m-%d %H:%M:%S") if book.get_date_borrowed() else "N/A"
            ))
    if not library.borrow_records:
        print("| {:<99} |".format("No borrowing records found."))
    print("+" + ("-" * 101) + "+")


if __name__ == "__main__":
    main()
