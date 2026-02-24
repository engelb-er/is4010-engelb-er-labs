class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a new Book object.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        Return a readable string representation of the Book.
        """
        return f"\"{self.title}\" by {self.author} ({self.year})"

    def get_age(self):
        """
        Return the age of the book assuming the current year is 2025.
        """
        current_year = 2025
        return current_year - self.year


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, file_size: int):
        """
        Initialize an EBook object, extending the Book class.
        """
        super().__init__(title, author, year)   # Call parent constructor
        self.file_size = file_size             # Add new attribute

    def __str__(self):
        """
        Return a readable string representation of the EBook,
        extending the Book's __str__ method.
        """
        parent_str = super().__str__()
        return f"{parent_str} ({self.file_size} MB)"


# ---- MAIN EXECUTION BLOCK ----
if __name__ == "__main__":
    # Test Book class
    sample = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    print(sample)
    print("Book age:", sample.get_age())

    # Test EBook class
    ebook_sample = EBook("Digital Fortress", "Dan Brown", 1998, 12)
    print(ebook_sample)
    print("EBook age:", ebook_sample.get_age())  # Should use inherited method