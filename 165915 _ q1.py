class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False



    
    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    



    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False



    
    def __str__(self):
        status = "borrowed" if self.is_borrowed else "available"
        return f"{self.title} by {self.author} ({status})"




class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []





    
    def borrow_book(self, book):

        if not book.is_borrowed:





            if book.mark_as_borrowed():
                self.borrowed_books.append(book)
                print(f"Successfully borrowed: {book.title}")
                return True

        print("Book is not available for borrowing.")
        return False


    
    def return_book(self, book):
        if   book in self.borrowed_books:
            if     book.mark_as_returned():
                self.borrowed_books.remove(book)



                print(f"Successfully returned: {book.title}")
                return True



        print("Book was not borrowed by this member.")
        return False
    
    def list_borrowed_books(self):


        if      not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:

            print(f"\n{self.name}'s borrowed books:")


            for book in self.borrowed_books:



                print(f"- {book.title} by {book.author}")

def main():



    #sample books
    books = [
        Book("Python Programming", "John Kinuthia"),
        Book("Data Structures", "Jane Wambari"),
        Book("Algorithms", "Alan Sanipei")
    ]
    
    # library member
    member = LibraryMember("Alice Kinuthia", "M001")
    
    while True:
        print("\n=== Library Management System ===")

        print("1. List all books")
        print("2. Borrow a book")

        print("3. Return a book")
        print("4. View borrowed books")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            print("\nAvailable Books:")
            for i, book in enumerate(books, 1):


                
                print(f"{i}. {book}")
                
        elif choice == "2":
            print("\nAvailable Books:")
            available_books = [book for book in books if not book.is_borrowed]
            for i, book in enumerate(available_books, 1):
                print(f"{i}. {book}")
            if available_books:
                try:
                    book_index = int(input("Enter book number to borrow: ")) - 1
                    if 0 <= book_index < len(available_books):
                        member.borrow_book(available_books[book_index])
                    else:
                        print("Invalid book number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No books available for borrowing.")
                
        elif choice == "3":
            if member.borrowed_books:
                print("\nYour Borrowed Books:")
                for i, book in enumerate(member.borrowed_books, 1):
                    print(f"{i}. {book}")
                try:
                    book_index = int(input("Enter book number to return: ")) - 1
                    if 0 <= book_index < len(member.borrowed_books):
                        member.return_book(member.borrowed_books[book_index])
                    else:
                        print("Invalid book number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("You have no books to return.")
                
        elif choice == "4":
            member.list_borrowed_books()
            
        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()