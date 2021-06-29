from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship('Post', backref='author', lazy='dynamic', cascade = 'all, delete, delete-orphan')
    liked = db.relationship('Like', backref='user', lazy='dynamic', cascade = 'all, delete, delete-orphan')

    def like_post(self, post):
        if not self.has_liked_post(post):
            like = Like(user_id=self.id, post_id=post.id)
            db.session.add(like)

    def unlike_post(self, post):
        if self.has_liked_post(post):
            Like.query.filter_by(user_id=self.id, post_id=post.id).delete()

    def has_liked_post(self, post):
        return Like.query.filter(Like.user_id == self.id, Like.post_id == post.id).count() > 0

    def delete_post(self, post):
        db.session.delete(post)
  
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password) 


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(140))
    country = db.Column(db.String(140))
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    likes = db.relationship('Like', backref='post', lazy='dynamic', cascade = 'all, delete, delete-orphan')

    def __repr__(self):
        return '<Post {}>'.format(self.description)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

# db.create_all()