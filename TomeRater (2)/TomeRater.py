# TomeRater Nick Lindenfelser


# Create a User
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Email Updated! New email address is {Updated_Email}.".format(Updated_Email=address))

    def __repr__(self):
        return ("User: {username}, Email: {email}, Books Read: {book_num}".format(username=self.name, email=self.email,
                                                                                book_num=len(self.books)))

    def __eq__(self, other):
        if (self.name == other.name) and (self.email == other.email):
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        value_int = 0
        book_number = 0
        for value in self.books.values():
            if value:
                value_int += value
                book_number += 1
        average = (value_int / book_number)
        return average

    def __hash__(self):
        return hash((self.name, self.email))

    def num_books_read(self):
        return len(self.books)


# Create a Book
class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.rating = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        print("ISBN Updated! New ISBN number is {New_ISBN}.".format(New_ISBN=new_isbn))

    def add_rating(self, rating_value):
        if (rating_value is not None) and (rating_value >= 0) and (rating_value <= 4):
            self.rating.append(rating_value)
        else:
            print("Invalid Rating")

    def __eq__(self, other):
        if (self.title == other.title) and (self.isbn == other.isbn):
            return True
        else:
            return False

    def get_average_rating(self):
        rating_score = 0
        for value in self.rating:
            rating_score += value
        if rating_score == 0:
            average_rating = 0
        else:
            average_rating = (rating_score / len(self.rating))
        return average_rating

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "Title: {TITLE} ISBN: {ISBN}".format(TITLE=self.title, ISBN=self.isbn)


# Fiction Subclass of Book
class Fiction(Book):
    def __init__(self, title, isbn, author):
        self.author = author
        super().__init__(title, isbn)

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{TITLE} by {AUTHOR}".format(TITLE=self.title, AUTHOR=self.author)


# Non-Fiction Subclass of Book
class Non_Fiction(Book):
    def __init__(self, title, isbn, subject, level):
        super().__init__(title, isbn)
        self.level = level
        self.subject = subject

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{TITLE}, a {LEVEL} manual on {SUBJECT}".format(TITLE=self.title, LEVEL=self.level, SUBJECT=self.subject)


# TomeRater
class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, isbn, author):
        fiction_book = Fiction(title, isbn, author)
        return fiction_book

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction_book = Non_Fiction(title, subject, level, isbn)
        return non_fiction_book

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            if rating is not None:
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("Error! No user with email: {EMAIL}".format(EMAIL=email))

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[email] = user
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    # Analysis Methods
    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.keys():
            print(user)

    def most_read_book(self):
        read_count = 0
        book_read = None
        for book, count in self.books.items():
            if count > read_count:
                read_count = count
                book_read = book
        return book_read

    def highest_rated_book(self):
        book_rating = 0
        book_rated = None
        for book in self.books.keys():
            if book_rating < book.get_average_rating():
                book_rating = book.get_average_rating()
                book_rated = book.title
        return book_rated

    def most_positive_user(self):
        user_rating = 0
        user_rated = None
        for user in self.users.values():
            user_average = user.get_average_rating()
            if user_average > user_rating:
                user_rating = user_average
                user_rated = user.name
        return user_rated

# Get Creative
    def get_n_most_read_books(self, n):
        most_books_read = []
        for book, value in self.books.items():
            most_books_read.append(book)
        return most_books_read[0:n]

    def get_n_most_prolific_readers(self, n):
        most_prolific_readers = []
        for user in self.users.values():
            prolific_readers = {user: user.num_books_read()}
        for user, value in prolific_readers.items():
            most_prolific_readers.append(user)
        return most_prolific_readers[:n]
