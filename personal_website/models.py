from personal_website import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# UserMixin provides default implementation of all needed user login methods
class User(db.Model, UserMixin):
    # unique userID
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)

    # toString
    def __repr__(self):
        return f'User \'{self.username}\' Email \'{self.email}\''
