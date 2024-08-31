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
    
    def view_available_books(self):
        return {bookid: details for bookid, details in self.books.items() if not details["is_borrowed"]}

def main() :
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Available Books")
        print("3. Borrow Book")
        
        choice = input("Enter your choice 1 or 2 or 3 : ")
        
        if choice == "1" :    
            bookid = input("Enter Book ID :")
            title = input("Enter Book Title :")
            author = input("Enter Book Writer name :")
            year = input("Enter year of publication :")
                
            library.add_book(bookid,title,author,year)
            print(f"Book '{title}' added successfully " )
            
        elif choice == "2" :
            available_books = library.view_available_books()
            if not available_books:
                print("No available books.")
            else:
                for bookid, details in available_books.items():
                    print(f"{details['title']} by {details['author']} (bookid: {bookid}, Year: {details['publication_year']})")
        
        elif choice == "3":
            bookid = input("Enter bookid of the book to borrow: ")
            try:
                library.borrow_book(bookid)
                print(f"Book with bookid {bookid} borrowed successfully.")
            except Exception as e:
                print(e)
                
if __name__ == "__main__":
    main()
print("run successfully")