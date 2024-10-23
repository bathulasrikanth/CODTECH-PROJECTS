from datetime import datetime, timedelta

class LibraryItem:
    def __init__(self, title, author, category, item_type):
        self.title = title
        self.author = author
        self.category = category
        self.item_type = item_type
        self.is_checked_out = False
        self.due_date = None

    def check_out(self, days):
        if not self.is_checked_out:
            self.is_checked_out = True
            self.due_date = datetime.now() + timedelta(days=days)
            print(f"{self.title} checked out successfully. Due on {self.due_date.date()}.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            overdue_days = (datetime.now() - self.due_date).days
            fine = 0
            if overdue_days > 0:
                fine = overdue_days * 2  # $2 fine for each day overdue
            self.is_checked_out = False
            self.due_date = None
            print(f"{self.title} returned successfully. Fine: ${fine}")
        else:
            print(f"{self.title} was not checked out.")

    def is_overdue(self):
        if self.is_checked_out and datetime.now() > self.due_date:
            return True
        return False

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"{self.item_type}: {self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, title, author, category, item_type):
        new_item = LibraryItem(title, author, category, item_type)
        self.items.append(new_item)
        print(f"{item_type} '{title}' added to the library.")

    def search_items(self, search_term, search_by="title"):
        results = []
        for item in self.items:
            if search_by == "title" and search_term.lower() in item.title.lower():
                results.append(item)
            elif search_by == "author" and search_term.lower() in item.author.lower():
                results.append(item)
            elif search_by == "category" and search_term.lower() in item.category.lower():
                results.append(item)
        return results

    def check_out_item(self, title, days):
        for item in self.items:
            if item.title.lower() == title.lower():
                item.check_out(days)
                return
        print(f"Item '{title}' not found in the library.")

    def return_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                item.return_item()
                return
        print(f"Item '{title}' not found in the library.")

    def list_overdue_items(self):
        overdue_items = [item for item in self.items if item.is_overdue()]
        if overdue_items:
            print("Overdue items:")
            for item in overdue_items:
                print(item)
        else:
            print("No items are overdue.")

    def display_items(self):
        for item in self.items:
            print(item)


# Usage example:
library = Library()

# Adding items
library.add_item("The Catcher in the Rye", "J.D. Salinger", "Fiction", "Book")
library.add_item("Time Magazine", "Various", "Magazine", "Magazine")
library.add_item("Inception", "Christopher Nolan", "Movie", "DVD")

# Searching for items
print("\nSearch by title:")
for item in library.search_items("Inception"):
    print(item)

print("\nSearch by author:")
for item in library.search_items("J.D. Salinger", "author"):
    print(item)

# Checking out and returning items
library.check_out_item("Inception", 7)  # Check out for 7 days
library.return_item("Inception")  # Return item

# Display all items in the library
print("\nAll items in the library:")
library.display_items()

# List overdue items
library.list_overdue_items()
