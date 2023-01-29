from sqlalchemy import Column, ForeignKey, String, INTEGER
from sqlalchemy.ext.declarative import declarative_base  

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(INTEGER, primary_key=True)
    email = Column(String)
    username = Column(String)
    password_hash = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    bio = Column(String)
    profile_pic = Column(String)

class Post(Base):
    __tablename__ = 'posts'
    post_id = Column(INTEGER, primary_key=True)
    link = Column(String)
    img = Column(String)
    title = Column(String)
    description = Column(String)
    score = Column(String)
    user_id = Column(INTEGER)

class Comment(Base):
    __tablename__ = 'comments'
    comment_id = Column(String, primary_key=True)
    user_id = Column(INTEGER)
    post_id = Column(INTEGER)
    comment_text = Column(String)
    comment_time = Column(String)

class Follow(Base):
    __tablename__ = 'followers'
    user_main = Column(INTEGER, primary_key=True)
    user_follower = Column(INTEGER, primary_key=True)

class Number(Base):
    __tablename__ = 'numbers'
    id = Column(INTEGER, primary_key=True)
    num = Column(INTEGER)