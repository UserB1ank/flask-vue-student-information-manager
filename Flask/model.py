from flask_sqlalchemy import *

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    avatar_path = db.Column(db.String(11), nullable=False)

    def __repr__(self):
        return "<User: %s, %s, %s, %s,%s>" % (self.id, self.username, self.password, self.phone, self.avatar_path)


# 学生信息对象
class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.String(10), primary_key=True, nullable=False)
    name = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(4), nullable=False)
    major = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    owner = db.relationship('User', backref=db.backref('posts', lazy='dynamic'))

    def __repr__(self):
        return "<User: %s, %s, %s, %s,%s>" % (self.id, self.name, self.gender, self.major, self.phone)
