from Flask_homework import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User: {self.id}"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Book: {self.title} {self.author}"


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User")
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    book = db.relationship("Book")
    date = db.Column(db.DateTime, nullable=False)

