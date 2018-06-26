# -*- coding:UTF-8 -*-
import requests
if __name__ == '__main__':
    target = 'https://github.com/laurel-he?tab=following'
    req = requests.get(url=target)
    fo = open('1.txt', "ab+")         #打开小说文件
    # 以二进制写入章节题目 需要转换为utf-8编码，否则会出现乱码  
    # 以二进制写入章节内容
    fo.write((req.text).encode('UTF-8'))  
    fo.close()        #关闭小说文件
