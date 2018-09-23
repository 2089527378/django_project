# encoding: utf-8
"""
从text写入neo4j
依据节点属性形成的树状图（属性同时为公司节点的子节点）
"""

from py2neo import Graph, Node, Relationship
def neo4jwrite2(texturl,password):
    file_handle = open(texturl, 'r')
    lines = file_handle.readlines()
    last = '*'
    db = Graph("http://localhost:7474/", username="neo4j", password=password)
    first = Node('UserClick', name='开始', time='', address='', pieaddress='')
    db.create(first)
    next1 = Node()
    for line in lines:
        print(line, type(line))
        result = line.split("***")
        print(result, len(result))
        nodeId = result[0].strip()
        nodeName = result[1]
        nodeTime = result[2]
        nodeAddress = result[3].strip()
        print('*' + nodeId + '*')
        if nodeId == '输入框节点:':
            a = Node('SelectNode', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='')
            db.create(a)
            relation = Relationship(first, 'Click', a)
            db.create(relation)

        if nodeId == '用户点击:':
            b = Node('UserClick', name=nodeName, time=nodeTime, address=nodeAddress, pieaddress='')
            db.create(b)
            relation = Relationship(next1, 'ClickList', b)
            db.create(relation)

        if nodeId == '公司节点:':
            db.run('match (n:comp) where n.name=\"%s\" return n.name,n.')
            c = Node('CompanyNode', name=nodeName, time=nodeTime, address=nodeAddress,)
            db.create(c)
            relation = Relationship(a, 'ClickCompany', c)
            db.create(relation)
            next1 = c

        if nodeId == '百度搜索框:':
            d = Node('BaiduNode', name=nodeName, time=nodeTime, address=nodeAddress)
            db.create(d)
            relation = Relationship(c, 'Baidu', d)
            db.create(relation)


if __name__ == '__main__':
     neo4jwrite2('F:\untitled2\\result2.txt', "123456")
