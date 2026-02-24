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


if __name__ == "__main__":
    # Test the Book class
    sample = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    print(sample)