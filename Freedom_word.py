# -*- coding:utf-8 -*-

# 替换单个词语，将敏感词替换成 Freedom，其他的替换成 Human Rights
# 参数 words 是 str 类型，表示想要替换的一句话
def freedom_word(words):
	# 将words 进行分词
	lword = words.split()
	# 读取敏感词列表并进行分词
	contents = open("filtered_words.txt").read()
	contents = contents.split()
	#print contents
	# 检查每一个输入的但此是否在敏感此列表中
	for word in lword:
		if word in contents:
			print " %s Freedom " % (word)
		else:
			print " %s Human Rights " % (word)

if __name__ == "__main__":
	words = raw_input("input what you want: ")
	freedom_word(words)
