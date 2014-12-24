# -*- coding: utf-8 -*-
import re

# 找 html 文件中的链接，现在利用的是 href 标记
# 接下来可以考虑用 http(s)/ftp 这些标记
# 这里主要考虑如何使用 re 工具包
# 参数 filename 为 html 文件名
def findLink(filename):
    file = open(filename)
    contents = file.read()
    linkre = re.compile("href=\"[^\"]*\"")
    c = re.findall(linkre, contents)
    for i in c:
        print i[5:]
    file.close()

if __name__ == "__main__":
    findLink("test.html")
