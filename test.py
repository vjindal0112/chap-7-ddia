from models import graph, directGraph
from models.models import User, Post, Comment
import csv



# User related functions
def add_user(user_id, email, username, password, firstname, lastname, bio):
    existing_user = graph.match(User).where(username=username).first()
    if existing_user:
        print("user already exists")
        return

    new_user = User()
    new_user.user_id = user_id
    new_user.email = email
    new_user.username = username
    new_user.password_hash = password # for demo, this would be hashd first
    new_user.firstname = firstname
    new_user.lastname = lastname
    new_user.bio = bio
    graph.save(new_user)

def get_user(user_id):
    return User.match(graph, user_id).first()

def get_following(user_id):
    user = User.match(graph, user_id).first()
    return user.follows # would have to turn into json using marshmellow or something

def set_password(user_id, new_password):
    user = User.match(graph, user_id).first()
    user.password = new_password #normally hash here, and do some checks etc

def delete_user(user_id):
    tx = directGraph.begin()
    tx.run("""
        MATCH (u:User) where u.user_id=$user_id DETATCH DELETE u
        """)
    tx.commit()
    return


##################################################################################################

# # make comments
# comments_file = open('wander_comments.csv', 'r')
# reader = csv.reader(comments_file)
# for row in reader:
#     comment = Comment()
#     comment.comment_id = row[0]
#     comment.user_id = row[1]
#     comment.post_id = row[2]
#     comment.comment_text = row[3]
#     comment.comment_time = row[4]
#     comment.post.add(Post.match(graph, comment.post_id).first())
#     comment.user.add(User.match(graph,comment.user_id).first())
#     graph.save(comment)
# print("comments saved")

# # make posts
# posts_file = open('wander_posts.csv','r')
# posts_reader = csv.reader(posts_file)
# for row in posts_reader:
#     post = Post()
#     post.post_id = row[0]
#     post.link = row[1]
#     post.img = row[2]
#     post.title = row[3]
#     post.description = row[4]
#     post.score = row[5]
#     post.user_id = row[6]
#     post.user.add(User.match(graph,post.user_id).first())
#     graph.push(post)
# print("posts are available")


# #make following edges
# follows_file = open('wander_follows.csv', 'r')
# reader = csv.reader(follows_file)

# follows_map = dict()
# for row in reader:
#     user_from = row[1]
#     user_to = row[0]
    
#     if not user_from in follows_map:
#         follows_map[user_from] = list()
#     follows_map[user_from].append(user_to)

# for user_from_id in follows_map:
#     user_from = User.match(graph, user_from_id).first()
#     for user_to_id in follows_map[user_from_id]:
#         user_to = User.match(graph, user_to_id).first()
#         user_from.follows.add(user_to)
#     graph.push(user_from)


# yash = User.match(graph, "2").first()
# yash.follows.add(yash)
# graph.push(yash)
# print(yash.firstname)

# # Fill the User table
# user_file = open('wander_users.csv', 'r')
# reader = csv.reader(user_file)
# for row in reader:
#     temp_user = User()
#     temp_user.user_id = row[0]
#     temp_user.email = row[1]
#     temp_user.username = row[2]
#     temp_user.password_hash = row[3]
#     temp_user.firstname = row[4]
#     temp_user.lastname = row[5]
#     temp_user.bio = row[6]
#     temp_user.profile_pic = row[7]
#     graph.push(temp_user)

# print("finished pushing users")


# usa = graph.match(Country, "USA").first()
# print(usa.name)

# nyc = City.match(graph, "nyc").first()
# for country in nyc.country:
#     print(country.name)

# from py2neo import Node, Relationship
# tx = g.begin()
# california = Node("State", name="California")
# tx.create(california)
# usa = Node("Country",name="USA")
# cal_usa = Relationship(california, "IN", usa)
# tx.create(cal_usa)
# tx.commit()
# print(g.run('MATCH (n), (usa) where usa.name="USA" and (n)-[:IN]->(usa) return n.name'))


# from neo4j import GraphDatabase
# class HelloWorldExample:
#     def __init__(self, uri, user, password):
#         self.driver = GraphDatabase.driver(uri, auth=(user, password))

#     def close(self):
#         self.driver.close()

#     def print_greeting(self, message):
#         with self.driver.session() as session:
#             greeting = session.execute_write(self._create_and_return_greeting, message)
#             print(greeting)

#     @staticmethod
#     def _create_and_return_greeting(tx, message):
#         # result = tx.run("CREATE (a:Greeting) "
#         #                 "SET a.message = $message "
#         #                 "RETURN a.message + ', from node ' + id(a)", message=message)

#         result = tx.run("MATCH (n) RETURN n")
#         return result
# if __name__ == "__main__":
#     greeter = HelloWorldExample("bolt://localhost:7687", "neo4j", "test")
#     greeter.print_greeting("hello, world")
#     greeter.close()