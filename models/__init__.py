from py2neo.ogm import Repository
from py2neo import Graph
from config import uri, username, password 

graph = Repository(uri, auth=(username, password))
directGraph = Graph(uri, auth=(username, password))