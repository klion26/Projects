# -*- coding: utf-8 -*-

# 统计纯文本文件中的单词个数
# 传入的参数 filename 表示纯文本文件的路径，这里用路径不用句柄，是因为打开和关闭应该在同一个地方进行
# 返回纯文本文件中的单词数目
def word_count(filename):
    # 打开文件
    file = open(filename)
    # 把整个文件都进来
    content = file.read().strip()
    # 根据空格进行分词（只考虑英文），这里 split 不用参数，会进行默认的分词，分割符包括 {空格，换行}
    word_list = content.split()
    # 输出中间结果，进行调试
    print word_list
    # 关闭文件
    file.close()
    # 返回单词数目
    return len(word_list)

if __name__ == "__main__":
    print word_count("test.txt")
