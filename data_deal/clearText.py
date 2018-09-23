# encoding: utf-8
"""
清空text文件
"""
def clearText(texturl):
    file = open(texturl,'r+')
    file.truncate()

# if __name__ == '__main__':
   # clearText('F:\untitled2\\result3.txt')