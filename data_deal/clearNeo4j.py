# encoding: utf-8
"""
清空neo4j数据库
"""
from py2neo import Graph, Node, Relationship
def clearNeo4j(password):
    db = Graph("http://localhost:7474/", username="neo4j", password=password)
    db.run("match p=()-[]->() delete p")
    db.run("match p=() delete p")

if __name__ == '__main__':
    clearNeo4j("123456")