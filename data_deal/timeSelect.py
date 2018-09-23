# encoding:utf-8
import operator as op
from py2neo import Graph
"""
将时间晚于输入时间的节点输出
"""
def time_lateSelect(str_time,password):
    db = Graph(password=password)
    data1 = db.run("match (n) return n.name,n.time").data()
    for i1 in data1:
        if i1['n.time'] and i1['n.time'] >= str_time:
             print(i1['n.time']+i1['n.name'])



"""
将时间早于输入时间的节点输出
 """
def time_ealierSelect(str_time,password):
    db = Graph(password=password)
    data1 = db.run("match (n) return n.name,n.time").data()
    for i1 in data1:
        if i1['n.time'] and i1['n.time'] <= str_time:
             print(i1['n.time']+i1['n.name'])

if __name__ == '__main__':
    time_lateSelect('2018/09/08 21:32:58', '123456')
    print('*' * 90)
    time_ealierSelect('2018/09/08 21:32:58', '123456')
