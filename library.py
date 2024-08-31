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
