
class User:
    def __init__(self, id: int, username: str):
        self.username = username
        self.user_id = id
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        for book in library.books_available[author]:
            if book == book_name:
                library.books_available[author].remove(book_name)
                self.books.append(book_name)
                if self.username not in library.rented_books:
                    library.rented_books[self.username] = {}
                    library.rented_books[self.username][book_name] = days_to_return
                library.rented_books[self.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        return f"The book \"{book_name}\" is already rented and " \
            f"will be available in {library.rented_books[self.username][book_name]} days!"

    def return_book(self, author: str, book_name: str, library):
        if book_name in library.rented_books[self.username]:
            library.rented_books[self.username].pop(book_name)
            library.books_available[author].append(book_name)
            self.books.remove(book_name)
            return
        return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"