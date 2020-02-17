from app import db

class Book(db.Model):

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Book: {self.title}>'
