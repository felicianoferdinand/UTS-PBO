import datetime

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrow_records = {}

    def add_book(self, book):
        self.books.append(book)

    def update_book(self, book_id, title, author, copies_available):
        for book in self.books:
            if book.get_book_id() == book_id:
                book.set_title(title)
                book.set_author(author)
                book.set_copies_available(copies_available)
                break

    def delete_book(self, book_id):
        self.books = [book for book in self.books if book.get_book_id() != book_id]

    def search_books(self, keyword):
        found_books = []
        for book in self.books:
            if keyword.lower() in book.get_title().lower() or keyword.lower() in book.get_author().lower():
                found_books.append(book)
        return found_books

    def add_member(self, member):
        self.members.append(member)

    def update_member(self, member_id, name, email):
        for member in self.members:
            if member.get_member_id() == member_id:
                member.set_name(name)
                member.set_email(email)
                break

    def delete_member(self, member_id):
        self.members = [member for member in self.members if member.get_member_id() != member_id]
    
    def borrow_book(self, member_id, book_id):
        # Check if book exists and available
        for book in self.books:
            if book.get_book_id() == book_id and book.get_copies_available() > 0:
                # Check if member exists
                for member in self.members:
                    if member.get_member_id() == member_id:
                        # Add borrowing record
                        if member_id not in self.borrow_records:
                            self.borrow_records[member_id] = {}
                        # Set date borrowed 
                        book.set_date_borrowed(datetime.datetime.now())
                        self.borrow_records[member_id][book_id] = book
                        # Update available copies
                        book.set_copies_available(book.get_copies_available() - 1)
                        return True
                return False
        return False

    def return_book(self, member_id, book_id):
        # Check if member has borrowed the book
        if member_id in self.borrow_records and book_id in self.borrow_records[member_id]:
            # Update available copies
            book = self.borrow_records[member_id][book_id]
            book.set_copies_available(book.get_copies_available() + 1)
            # Remove borrowing record
            del self.borrow_records[member_id][book_id]
            if not self.borrow_records[member_id]:  # If no more borrowed books, remove member from records
                del self.borrow_records[member_id]
            return True
        return False
    