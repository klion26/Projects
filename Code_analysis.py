# -*- coding: utf-8 -*-

# 统计文件中的代码，注释，以及空行数目
# filename 表示输入文件的文件名
def codeAnalysis(filename):
    # 打开文件
    file = open(filename)
    # codeLine：代码行数
    # emptyLine 空行数目
    # commentLine 注释行数
    codeLine = 0
    emptyLine = 0
    commentLine = 0
    content = file.readline()
    while content :
        content = content.strip()
        # 如果是空行
        if content == '':
            emptyLine += 1
        # 如果是注释，只考虑单行注释。后期可以考虑添加其他的注释类型
        elif content[0] == '#':
            commentLine += 1
        else: # 代码
            codeLine += 1
        content = file.readline()
    # 关闭文件
    file.close()
    # 对统计信息进行输出
    print "Code line %d" % codeLine
    print "Empty line %d" % emptyLine
    print "Comment line %d" % commentLine

if __name__ == "__main__":
    codeAnalysis("test.txt")
