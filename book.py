class Book:
    def __init__(self, book_id, title, author, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies_available = copies_available
        self.date_borrowed = None

    def get_book_id(self):
        return self.book_id

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_copies_available(self):
        return self.copies_available
    
    def get_date_borrowed(self):
        return self.date_borrowed

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_copies_available(self, copies_available):
        self.copies_available = copies_available

    def set_date_borrowed(self, date_borrowed):
        self.date_borrowed = date_borrowed
