# date:2018/9/22 9:27
# -*- coding: utf-8 -*-
#author;cwd
"""
function:image is saved in images_Path_save
"""
from matplotlib import pyplot as plt
import os
def makePie(images_Path_save,image_name):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    images_Path_save = "./image_save"
    image_name = "tengxun.jpg"
    image_Path_save = os.path.join(images_Path_save, image_name)
    plt.figure(figsize=(6, 9))
    labels = [u'公司名称：腾讯公', u'法人：孙艳芳', u'公司地址：辽源路从十分丰富威风威风威风威风',
              u'主营方向: 计算机软件', u'信用网址：www23233.com', u'商务网址：sdaadiddd.com']
    sizes = [10, 10, 10, 10, 10, 10]
    colors = ['red', 'yellowgreen', 'lightskyblue', 'blue', 'gray', 'orange', 'green']
    explode = (0, 0, 0, 0, 0, 0)
    patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                                      labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                      startangle=90, pctdistance=0.6)
    for t in l_text:
        t.set_size = (30)
    for t in p_text:
        t.set_size = (20)
    plt.axis('equal')
    plt.legend()
    plt.savefig(image_Path_save)

makePie('','')