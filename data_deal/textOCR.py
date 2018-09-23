# coding:utf-8
"""
识别用户点击的连通域，进行OCR识别，并对识别结果进行处理，关系的粗略确定
"""
from PIL import Image
from numpy import *
import cv2
from skimage import measure
from aip import AipOcr
import sys
import  os.path
reload(sys)
sys.setdefaultencoding( 'utf-8' )

def filenamesplit(filename):
    c=filename.split('_')
    time_y = c[1]
    time_m = c[2]
    time_d = c[3]
    time_h = c[4]
    time_M = c[5]
    time_s = c[6].split('(')[0]
    a = filename.split('(')[1]
    b = a.split(')')[0]
    x = b.split(',')[0]
    y = b.split(',')[1]
    return int(x), int(y), [time_y, time_m, time_d, time_h, time_M, time_s]

def filenameSplit(filename):
    a = filename.split('(')[1]
    b = a.split(')')[0]
    x = b.split(',')[0]
    y = b.split(',')[1]
    return int(x), int(y)

def imfill(im_in):
    size = im_in.shape
    m = size[0]
    n = size[1]
    im_out = zeros([m, n])
    im2, contours, hierarchy = cv2.findContours(im_in, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0 and len(hierarchy) != 0:
        for i in range(len(contours)):
            cv2.drawContours(im_out, contours, i, 255, cv2.FILLED)

    return im_out
def min3(a,b,c):
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    return min


def erzhihua(I):

    size = I.shape
    m = size[0]
    n = size[1]
    k = size[2]
    r = I[:,:,0]
    g = I[:, :, 1]
    b = I[:, :, 2]
    im = zeros([m, n])
    im1 = zeros([m, n])
    for i in range(m):
        for j in range(n):
            im[i, j] = min3(r[i, j], g[i, j], b[i, j])

    for i in range(m):
        for j in range(n):
            if im[i, j] > 255*0.7:
                im1[i, j] = 255
    return im1

def rlsa(im1):
    size = im1.shape
    m = size[0]
    n = size[1]
    count1 = zeros([m, 1])
    for i in range(m):
        for j in range(n-1):
            if (im1[i, j] == 255)and(im1[i, j+1] == 255):
                count1[i] = count1[i]+1
            if (im1[i, j] == 255)and(im1[i, j+1] == 0):
                if count1[i] <= 8:
                    for l in range(j-int(count1[i]),j+1):
                        im1[i, l] = 0
                count1[i] = 0

    count2 = zeros([n, 1])
    for j in range(n):
        for i in range(m-1):
            if (im1[i, j] == 255)and(im1[i+1, j] == 255):
                count2[j] = count2[j]+1
            if (im1[i, j] == 255)and(im1[i+1, j] == 0):
                if count2[j] <= 2:
                    for l in range(i-int(count2[j]), i+1):
                        im1[l, j] = 0
                count2[j] = 0
    return im1

def saixuan(im1):
    size = im1.shape
    m = size[0]
    n = size[1]
    labelimg, num = measure.label(im1, None, None, True, connectivity=1)
    props = measure.regionprops(labelimg)

    hww = []
    zhoucb = []
    while(num):
        num = num - 1
        c1 = []
        r = []
        for i in range(m):
            for j in range(n):
                if labelimg[i, j] == num:
                    r.append(i)
                    c1.append(j)

        left = min(r)
        right = max(r)
        bottom = max(c1)
        top = min(c1)
        hww.insert(num, (right-left+1)/(bottom-top+1))
        zhoucb.insert(num, (props[num]['perimeter'])/(((right-left+1)+(bottom-top+1))*2))
    return props, hww, zhoucb

def saixuan1(im1, mouse_x, mouse_y):
    im2, contours, hierarchy = cv2.findContours(im1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)

    im3 = zeros([im1.shape[0], im1.shape[1]])
    isb = zeros([len(contours), 1])
    lty_x = 0
    lty_y = 0
    lty_w = 100
    lty_h = 100
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        area = cv2.contourArea(contours[i])
        zhoucb = cv2.arcLength(contours[i], True)/(w+h)/2
        kgb = w/h
        if mouse_x >= x-2 and mouse_x <= (x+w+2) and mouse_y >= y-2 and mouse_y <= (y+h+2):
            isb[i] = 1
        if isb[i] == 1 and area > 10 and zhoucb < 1.3 and zhoucb > 0.9 and kgb >2.0and kgb < 50:#if isb[i] == 1 and area > 100 and zhoucb >0.8 and zhoucb<2 and kgb >=2 and kgb < 30:#if isb[i] == 1 and area > 10 and zhoucb < 1.3 and zhoucb > 0.9 and kgb > 5 and kgb < 30:  #if   isb[i]==1 :#if isb[i] == 1 and zhoucb < 1.3 and zhoucb > 0.9 and kgb > 5 and kgb < 30:#if isb[i] == 1 and area < (im1.shape[0] * im1.shape[1])/3:#if isb[i] == 1 and area > 10000 and zhoucb < 1.3 and zhoucb > 0.9 and kgb > 5 and kgb < 30:#if   isb[i]==1 :
            cv2.drawContours(im3, contours, i, 255, 1)
            cv2.rectangle(im3, (x, y), (x+w, y+h), 100, 2)
            lty_x = x
            lty_y = y
            if(w <=15 or h <= 15):
                 lty_w = w + 15
                 lty_h = h + 15
            else:
                lty_w = w
                lty_h = h
        else:
            cv2.drawContours(im3,contours, i,  0, 1)

    return im3, contours, lty_x, lty_y, lty_w, lty_h

def mycopy(im_in,I):
    size = im_in.shape
    m = size[0]
    n = size[1]
    im_out = zeros([m, n])
    for i in range(m):
        for j in range(n):
            a = I[i, j]
            if im_in[i, j] == 255:
                im_out[i, j] = a

    return im_out
def zonghe(filename1,x,y):
    I = Image.open(filename1)
    im6 = I.convert('L')
    I = array(I)
    im6 = array(im6)
    im1 = erzhihua(I)
    im4 = rlsa(im1)
    #im10=Image.fromarray(im4)
    #im10.show()
    im5 = uint8(im4)
    im5 = 255 - im5
    im5 = imfill(im5)
    #im10 = Image.fromarray(im5)
    #im10.show()
    im5 = uint8(im5)
    im3, contours, lty_x, lty_y, lty_w, lty_h = saixuan1(im5, x, y)
    im3 = uint8(im3)
    im3 = imfill(im3)
    #im10 = Image.fromarray(im3)
    #im10.show()
    im3 = mycopy(im3, im6)
    #im10 = Image.fromarray(im3)
    #im10.show()
    im3 = Image.fromarray(im3)
    im3 = im3.crop((lty_x, lty_y, lty_x+lty_w, lty_y+lty_h))
    im3 = array(im3)
    return im3

def OCR(filename):
    APP_ID = '11418443'
    API_KEY = 'od6MXy9DvM3TTvHVpIsalgSO'
    SECRET_KEY = '1eoLKrIvpts8oKOysNfDvtK9nVffxCnD '
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "true"

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    string = []
    image = get_file_content(filename)
    result = {}
    result = client.basicAccurate(image, options)
    # print(result['words_result'])
    for i in range(len(result['words_result'])):
        string.append(result["words_result"][i]["words"])

    return string




#
"""
file_img:截图存放文件夹url
text_url:返回结果text文件url
file_result:处理结果图像存放文件夹url
"""
def textOCR(file_img,text_url,file_result):
    filename_in = file_img
    cont = -1
    cont2 = 0
    str5 = ''
    for parent, dirnames, filenames in os.walk(filename_in):
        for filename in filenames:
            file_handle = open(text_url, 'a+')
            filename_out = file_result
            # filename = os.path.join(parent,filename)
            time = []
            x, y, time = filenamesplit(filename)
            file_in = filename_in + filename
            file_out = filename_out + filename
            im3 = zonghe(file_in, x, y)
            print("step  one is ok")
            cv2.imwrite(file_out, im3)
            print("step  two is ok")
            str1 = []
            str1 = OCR(file_out)

            str2 = time[0] + "/" + time[1] + "/" + time[2] + " " + time[3] + ":" + time[4] + ":" + time[5]
            str4 = ''
            for i in range(len(str1)):
                str4 = str4 + str1[i] + ' '
            if len(str4) != 0 and '公司' in str4:

                if (str4 == str5) == False or (str5.split('公')[0] == str4.split('公')[0]) == False:
                    cont = 1
                    file_handle.write(
                        str(cont) + "***" + str4 + "***" + str2 + "***" + filename_in + filename + "***" + "\n")

            if len(str4) != 0 and '公司' not in str4 and '搜索' not in str4:

                if str4 != str5:
                    cont = cont + 1
                    file_handle.write(
                        str(cont) + "***" + str4 + "***" + str2 + "***" + filename_in + filename + "***" + "\n")
            if len(str4) != 0 and '公司' not in str4 and '搜索' in str4:

                if str4 != str5:
                    cont = 0
                    file_handle.write(
                        str(cont) + "***" + str4 + "***" + str2 + "***" + filename_in + filename + "***" + "\n")
            file_handle.close()
            str5 = str4
            print("end")

# if __name__ == '__main__':
    # textOCR('F:\\untitled2\\img\\', 'F:\\untitled2\\result3.txt', 'F:\\untitled2\\result\\')










