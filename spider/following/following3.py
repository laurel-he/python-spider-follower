# -*- coding:UTF-8 -*-
import requests
import re
if __name__ == '__main__':
    target = 'https://github.com/laurel-he?after=Y3Vyc29yOnYyOpKpd3V5YW94aW5nzgGOAYw%3D&tab=following'
    req = requests.get(url=target)
    context = req.text
    patt = re.compile(r"data-octo-dimensions=\"link_type:self\".*href=\"/(.*?)\"")
    ch = patt.findall(req.text)
    fo = open('following3.txt',"ab+")
    for i in ch:
        line = str(i) + "\n"
        fo.write((line).encode('UTF-8')+b'\r\n')
    fo.close
