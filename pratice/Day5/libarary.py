class Library:
    def add_book(self):
        print("Book added")

    def remove_book(self):
        print("Book removed")

    def display_books(self):
        print("Available books:")
        print("1. Python")
        print("2. Java")
        print("3. Data Structures")


l1 = Library()

l1.add_book()
l1.display_books()
l1.remove_book()