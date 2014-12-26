# -*- coding: utf-8 -*-
import xlwt, re, binascii

# 处理一行数据，把这行数据分离出来
# 传入的参数表示一整行数据
def process(line):
    # 找到表示 no 的正则表达式
    no = re.compile('"[\d]*"')
    n = re.findall(no, line)
    # 去掉 no 两边的引号
    n = n[0][1:-1]
    # 找到剩余数据的正则表达式
    info = re.compile(':\[.*\]')
    infomation = re.findall(info, line)
    # 去掉中括号
    infomation = infomation[0][2:-1]
    #print infomation
    # 将数据分割成单个的数据记录
    infomation = infomation.split(',')
    # 去掉名字两边的引号
    name = infomation[0][1:-1]
    # 将有引号的名字替换成没有引号的名字
    infomation.pop(0)
    infomation.insert(0, name)
    # 输出信息，用于调试
    print infomation
    # 将 no 插入到数据中，形成一整条数据
    infomation.insert(0, n)
    return infomation

# 将数据存入 xls 文件中，
# 参数 contents 表示将要存入的数据
# 参数 filname 表示 xls 的文件名
def writexls(contents, filename):
    # 这里创建 Workbook 实例的时候需要带编码格式，默认的 ascii 不能处理中文
    data = xlwt.Workbook(encoding='gb2312')
    table = data.add_sheet('infomation')
    row = 0
    for i in contents:
        col = 0
        for j in i:
            # 将当前数据添加到 (row, col) 位置处
            table.write(row, col, j)
            col += 1
        row += 1
    #保存 xls 文件
    data.save(filename)
    
if __name__ == "__main__":
    file = open("student.txt")
    line = file.readline()
    contents = []
    while line:
        # 去掉前后的空格，换行等字符
        line = line.strip()
        # 如果不是 '{' 和 '}'
        if line != "{" and line != "}":
            contents.append(process(line))
        # 读取下一行
        line = file.readline()
    writexls(contents, "student.xls")
    print contents
