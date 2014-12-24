# -*- coding: utf-8 -*- 
import  re

# 找到一个 html 文件中的 body 部分
# 现在找到的部分，包括 <body> </body> 两个标签，后期可以考虑怎么去掉这两个标签
# filename 表示 html 文件的文件名
def findBody(filename):
    file = open(filename)
    contents = file.read()
    #print contents
	# begin 表示 body 部分的正则表达式
    begin = re.compile("<body[\s\S]*</body>")#[^>]*>")#[\s.]*</body>")
	# 利用 begin 找到 body 部分
    start = re.findall(begin, contents)
    #print start
	# 将 body 部分写入文件
    writeFile = open("body.html", "w")
    for i in start:
        writeFile.write(i)
    writeFile.close()
    file.close()

if __name__ == "__main__":
	findBody("test.html")
