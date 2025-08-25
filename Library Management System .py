import datetime

# Data storage
books = {}
members = {}
borrowed_books = {}

# ------------------- Book Functions -------------------
def add_book(book_id, title, author, quantity):
    books[book_id] = {"title": title, "author": author, "quantity": quantity}
    print(f"Book '{title}' added successfully!")

def update_book(book_id, title=None, author=None, quantity=None):
    if book_id in books:
        if title: books[book_id]["title"] = title
        if author: books[book_id]["author"] = author
        if quantity is not None: books[book_id]["quantity"] = quantity
        print("Book updated successfully!")
    else:
        print("Book not found!")

def delete_book(book_id):
    if book_id in books:
        del books[book_id]
        print("Book deleted successfully!")
    else:
        print("Book not found!")

def search_book(keyword):
    found = [book for book in books.values() if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]
    if found:
        for b in found:
            print(b)
    else:
        print("No books found!")

# ------------------- Member Functions -------------------
def register_member(member_id, name, contact):
    members[member_id] = {"name": name, "contact": contact}
    print(f"Member '{name}' registered successfully!")

# ------------------- Borrow/Return Functions -------------------
def borrow_book(book_id, member_id):
    if book_id not in books:
        print("Book not found!")
        return
    if books[book_id]["quantity"] <= 0:
        print("Book not available!")
        return
    
    due_date = datetime.date.today() + datetime.timedelta(days=14)
    borrowed_books[(book_id, member_id)] = due_date
    books[book_id]["quantity"] -= 1
    print(f"Book borrowed successfully! Due date: {due_date}")

def return_book(book_id, member_id):
    if (book_id, member_id) in borrowed_books:
        del borrowed_books[(book_id, member_id)]
        books[book_id]["quantity"] += 1
        print("Book returned successfully!")
    else:
        print("This book was not borrowed by the member!")

# ------------------- Utility Functions -------------------
def view_books():
    for book_id, details in books.items():
        print(book_id, details)

def view_members():
    for member_id, details in members.items():
        print(member_id, details)

# ------------------- Example Run -------------------
if __name__ == "__main__":
    add_book(1, "Harry Potter", "J.K. Rowling", 5)
    add_book(2, "The Hobbit", "J.R.R. Tolkien", 3)

    register_member(101, "Alice", "alice@email.com")
    register_member(102, "Bob", "bob@email.com")

    view_books()
    borrow_book(1, 101)
    view_books()
    return_book(1, 101)
    view_books()





