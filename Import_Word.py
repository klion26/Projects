# -*- coding:utf-8 -*-

# Method-A
# 找到文件中出现次数最多的那个单词
# filename 是输入的文件名
def import_Word(filename):
    # 打开文件
    f = open(filename)
    # 读取文件，以及去掉前后的空格
    content = f.read().strip()
    # 将文件中的单词分割开来
    content = content.split(' ')
    # words 是 dict 对象，{单词：出现次数}键值对
    words = {}
    # 统计每个单词出现的次数
    for word in content:
        if word in words:
            words[word] = words[word]+1
        else:
            words[word] = 1
    print words
    # 查找出现次数最多的单词，使用依次寻找的方法
    # maxNum 表示单词出现最多的次数
    maxNum = 1
    for word in words:
        # 如果当前单词出现的次数比 maxNum 大，则更新
        if words[word] > maxNum:
            maxWord = word
            maxNum = words[word]
    # 输出出现最多的次数，同时可以输出相应的单词
    print maxWord, maxNum
    # 关闭文件
    f.close()

# Method-B
# 和 Method-A 的区别在于最后找出现次数最多的单词处
# 找到文件中出现次数最多的那个单词
# filename 是输入的文件名
def import_Word(filename):
    # 打开文件
    f = open(filename)
    # 读取文件，以及去掉前后的空格
    content = f.read().strip()
    # 将文件中的单词分割开来
    content = content.split(' ')
    # words 是 dict 对象，{单词：出现次数}键值对
    words = {}
    # 统计每个单词出现的次数
    for word in content:
        if word in words:
            words[word] = words[word]+1
        else:
            words[word] = 1
    print words
    # 这里将 words 中的键值互换，然后用互换后的键进行从大到小的排序，最后输出第一个（也就是最大的）元素的值（原 dict 中的键）
    print sorted([(counter, word) for word, counter in words.items()], reverse=True)[0][1]
    # 关闭文件
    f.close()

if __name__ == "__main__":
    import_Word("test.txt")
