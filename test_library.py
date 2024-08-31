import unittest
from library import Library 

# Test case for the add_book method
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
        
if __name__ == "__main__":
    unittest.main()
    