# coding:utf-8
from numpy import *
import sys
import os.path

"""
清空file_url文件夹下的jpg、png、bmp格式的图片
"""
def clearFile(file_url):
        for root, dirs, files in os.walk(file_url):
            for name in files:
                if name.endswith(".png")or name.endswith(".jpg")or name.endswith(".bmp"):
                    os.remove(os.path.join(root, name))
                    print ("Delete File: " + os.path.join(root, name))

# if __name__ == '__main__':
    # clearFile("F:/wo/")