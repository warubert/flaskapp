from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50))
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<User: username={self.username}, role={self.role}>'

    def get_id(self):
        return self.uid
class Person(db.Model):
    __tablename__ = 'people'
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.Text)

    def __repr__(self):
        return f'Person(pid={self.pid}, name={self.name}, age={self.age}, job={self.job})'