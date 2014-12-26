# -*- coding: utf-8 -*-
import random, string

# 生成长度为 randomlength 的随机字符串，字符串中包括的字符有 'a-zA-Z0-9'
# randomlength 为字符串的长度，默认为8
def random_str(randomlength=8):
    # str 为返回的字符串
    str = ''
    # chars 为随机字符串中会出现的字符
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    # 生成 randomlength 个随机字符
    for i in xrange(randomlength):
        str += chars[random.randint(0, length)]
    return str

# 另外一种生成长度为 randomlength 的随机字符串 字符中包括的字符可以有 'a-zA-Z0-9'
# randomlength 为字符串长度，默认为8
def random_str2(randomlength=8):
    # 先生成字符串列表
    a = list(string.ascii_letters)
    a += list(string.digits)
    #print a
    # 对字符串列表进行原地洗牌，打乱顺序
    random.shuffle(a)
    # 取前 randomlength 个字符作为最后的结果
    return ''.join(a[:randomlength])

# 第三种方法
def random_str3(randomlength=8):
    return ''.join(random.sample(string.ascii_letters+string.digits, randomlength))
if __name__ == "__main__":
    for i in xrange(20):
        print random_str(), random_str2(), random_str3()
