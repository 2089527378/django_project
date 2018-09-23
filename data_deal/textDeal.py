# encoding: utf-8
"""
对返回的text文档进行进一步处理，识别出公司节点、输入框节点、百度搜索框节点、用户点击节点
"""
def textDeal(text_in,text_out):
    file = open(text_out, 'r')
    file_in = open(text_in, 'a+')
    lines = file.readlines()
    line_lastcom = "*"
    line_last = '*'
    for line in lines:
        lineStr = line.split('***')
        line_a = lineStr[0]
        line_b = lineStr[1].rstrip()
        # print(line_b)
        line_c = lineStr[2].strip()
        line_d = lineStr[3].strip()
        if (line_b.endswith('公司') or line_b.endswith('酒店') or line_b.endswith('工厂')) and (
                line_lastcom not in line_b and line_lastcom != line_b):
            line_lastcom = line_b
            print("公司节点: " + line_b + "***时间戳：" + line_c + "***图片路径：" + line_d)
            file_in.write("公司节点:***" + line_b + "***" + line_c + "***" + line_d + "***\n")
        else:
            if line_b.endswith('百度一下') or "百度一下" in line_b or "搜一下" in line_b:
                print("百度搜索框: " + line_b + " 时间戳:" + line_c + " 图片路径:" + line_d + "\n")
                file_in.write("百度搜索框:***" + line_b + "***" + line_c + "***" + line_d + "***\n")
            else:
                if line_b.endswith('搜索') or line_b.endswith('搜索一下'):
                    line_last = line_b
                    print("输入框节点:***" + line_b + " 时间戳：" + line_c + " 图片路径：" + line_d)
                    file_in.write("输入框节点:***" + line_b + "***" + line_c + "***" + line_d + "***\n")
                else:
                    if "输入企业法定代表人" in line_last:
                        print("法人节点：" + line_b + " 时间戳：" + line_c + " 图片路径：" + line_d)
                        file_in.write("法人节点:***" + line_b + "***" + line_c + "***" + line_d + "***\n")
                    else:
                        print("用户点击：" + line_b + " 时间戳：" + line_c + " 图片路径：" + line_d)
                        file_in.write("用户点击:***" + line_b + "***" + line_c + "***" + line_d + "***\n")

if __name__ == '__main__':
    textDeal('F:\\untitled2\\result2.txt', '.\\result3.txt')







