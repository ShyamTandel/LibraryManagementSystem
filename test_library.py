import unittest
from library import Library 

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("1", "Basic Maths", "shyam", "2023")
        self.assertIn("1", self.library.books)
        self.assertEqual(self.library.books["1"]["title"], "Basic Maths")

    def test_borrow_book(self):
        self.library.add_book("1", "Basic Maths", "shyam", "2023")
        self.library.borrow_book("1")
        self.assertTrue(self.library.books["1"]["is_borrowed"])
        
    def test_return_book(self):
        self.library.add_book("1", "Basic Maths", "shyam", "2023")
        self.library.borrow_book("1")
        self.library.return_book("1")
        self.assertFalse(self.library.books["1"]["is_borrowed"])
    
    def test_view_available_books(self):
        self.library.add_book("1", "Basic Maths", "shyam", "2023")
        self.library.add_book("2", "Advanced Maths", "shyam", "2024")
        self.library.borrow_book("1")
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 1)
        self.assertIn("2", available_books)

if __name__ == "__main__":
    unittest.main()
    