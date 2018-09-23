# encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
from textOCR import textOCR
textOCR('F:\\untitled2\\img\\', 'F:\\untitled2\\result3.txt', 'F:\\untitled2\\result\\')

from neo4j import neo4jwrite
neo4jwrite('F:\untitled2\\result2.txt', "123456")
from neo4j2 import neo4jwrite2
neo4jwrite2('F:\untitled2\\result2.txt', "123456")

from neo4j3 import neo4jwrite3
neo4jwrite3('F:\untitled2\\result2.txt', "123456")

from clearNeo4j import clearNeo4j
clearNeo4j("123456")

from clearText import clearText
clearText('F:\untitled2\\result2.txt')
"""
from clearNeo4j import clearNeo4j
from neo4j import neo4jwrite
from neo4j2 import neo4jwrite2
from neo4j3 import neo4jwrite3
clearNeo4j('123456')
neo4jwrite('F:/untitled2/result2.txt', "123456")
#
"""
from py2neo import Graph
db = Graph("http://localhost:7474/", username="neo4j", password="123456")
j = 50
str1 = '开始'
str2 = ''
while j:
    data1 = db.run("match (start)-[]->(n) where start.name='%s'and start.time='%s' return n.name,n.time,n.address" % ( str1, str2)).data()
    for i1 in range(len(data1)):
        str1 = data1[i1]['n.name']
        str2 = data1[i1]['n.time']
        str3 = data1[i1]['n.address']
        print str1+str2+str3
    j = j-1
"""