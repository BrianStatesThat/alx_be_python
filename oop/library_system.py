class Book:
    def __init__(self, title: str, author: str):
        """Initialize base Book with title and author."""
        self.title = title
        self.author = author

    def get_details(self):
        """Return formatted details string for Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize EBook with additional file_size attribute."""
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def get_details(self):
        """Return formatted details string for EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize PrintBook with additional page_count attribute."""
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        """Return formatted details string for PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize Library with an empty list of books."""
        self.books = []

    def add_book(self, book: Book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library in the required format."""
        for book in self.books:
            print(book.get_details())