import unittest

# Sample Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {"title": title, "author": author}
        self.books.append(book)
        return book
    
# Test case for the add_book method
class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book_success(self):
        book = self.library.add_book("2022", "Basic Maths")
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(book["title"], "2022")
        self.assertEqual(book["author"], "Basic Maths")

if __name__ == "__main__":
    unittest.main()
    