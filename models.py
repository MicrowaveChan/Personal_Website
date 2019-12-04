from app import db

class User(db.Model):
    # unique userID
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)

    # toString
    def __repr__(self):
        return f'User {self.username}'
