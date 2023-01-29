from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from sqlModels import db
from sqlModels.models import User, Post, Comment, Follow
import csv

def loadUsers():
    Session = sessionmaker(db)
    session = Session()
    users_file = open('wander_users.csv', 'r')
    reader = csv.reader(users_file)
    for row in reader:
        user = User()
        user.user_id = row[0]
        user.email = row[1]
        user.username = row[2]
        user.password_hash = row[3]
        user.firstname = row[4]
        user.lastname = row[5]
        user.bio = row[6]
        user.profile_pic = row[7]
        session.add(user)
    session.commit()

def loadPosts():
    Session = sessionmaker(db)
    session = Session()
    posts_file = open('wander_posts.csv','r')
    posts_reader = csv.reader(posts_file)
    for row in posts_reader:
        post = Post()
        post.post_id = int(row[0])
        post.link = row[1]
        post.img = row[2]
        post.title = row[3]
        post.description = row[4]
        post.score = float(row[5]) if row[5] else 0
        post.user_id = int(row[6])
        session.add(post)
    session.commit()

def loadComments():
    Session = sessionmaker(db)
    session = Session()
    comments_file = open('wander_comments.csv','r')
    comments_reader = csv.reader(comments_file)
    for row in comments_reader:
        comment = Comment()
        comment.comment_id = int(row[0])
        comment.user_id = int(row[1])
        comment.post_id = int(row[2])
        comment.comment_text = row[3]
        comment.comment_time = row[4]
        session.add(comment)
    session.commit()

def loadFollows():
    Session = sessionmaker(db)
    session = Session()
    follows_file = open('wander_follows.csv','r')
    follows_reader = csv.reader(follows_file)
    for row in follows_reader:
        follow = Follow()
        follow.user_main = int(row[0])
        follow.user_follower = int(row[1])
        session.add(follow)
    session.commit()

loadFollows()