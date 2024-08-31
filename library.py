class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, bookid, title, author, publication_year):
        if bookid in self.books:
            raise Exception(f"Book with bookid {bookid} already exists.")
        self.books[bookid] = {
            "title": title,
            "author": author,
            "publication_year": publication_year,
            "is_borrowed": False
        }
        
    def borrow_book(self, bookid):
        if bookid not in self.books:
            raise Exception(f"Book with bookid {bookid} does not exist.")
        if self.books[bookid]["is_borrowed"]:
            raise Exception(f"The book '{self.books[bookid]['title']}' is currently unavailable.")
        self.books[bookid]["is_borrowed"] = True

    def return_book(self, bookid):
        if bookid not in self.books:
            raise Exception(f"Book with bookid {bookid} does not exist.")
        if not self.books[bookid]["is_borrowed"]:
            raise Exception(f"The book '{self.books[bookid]['title']}' is not borrowed.")
        self.books[bookid]["is_borrowed"] = False
