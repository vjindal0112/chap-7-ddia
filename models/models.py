from ast import Mod
from curses.ascii import US
from py2neo.ogm import *

class User(Model):
    __primarykey__ = "user_id"

    user_id = Property()
    email = Property()
    username = Property()
    password_hash = Property()
    firstname = Property()
    lastname = Property()
    bio = Property()
    profile_pic = Property()

    follows = RelatedTo("User", "FOLLOWS")
    followed_by = RelatedFrom("User", "FOLLOWS")

class Post(Model):
    __primarykey__= "post_id"

    post_id = Property()
    link = Property()
    img = Property()
    title = Property()
    description = Property()
    score = Property()
    user_id = Property()

    user = RelatedTo(User, "BELONGS_TO")

class Comment(Model):
    __primarykey__ = "comment_id"
    comment_id = Property()
    user_id = Property()
    post_id = Property()
    comment_text = Property()
    comment_time = Property()

    post = RelatedTo(Post,"BELONGS_TO")
    user = RelatedTo(User, "BELONGS_TO")

# class Country(Model):
#     __primarykey__ = "name"
#     name=Property()
#     size=Property()


#     cities = RelatedFrom("City" = Property() "IN")
#     districts = RelatedFrom("District" = Property() "IN")
#     states = RelatedFrom("State" = Property() "IN")

# class City(Model):
#     __primarykey__ = "name"
#     name=Property()
#     country = RelatedTo(Country = Property() "IN")

# class District(Model):
#     __primarykey__ = "name"
#     name=Property()

# class State(Model):
#     __primarykey__ = "name"
#     name=Property()
