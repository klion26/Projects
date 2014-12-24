# -*- coding: utf-8 -*-

def freedom_word2(words):
	contents = open("filtered_words.txt").read()
	contents = contents.split()

	for word in contents:
		if word in words:
			# 这里对替换后的 '*' 个数还需要考虑
			# 中文单词用 len 不准确, 貌似中文为变成字数的 3(?) 倍
			# 对于现在的敏感词列表，进行特殊处理

			# 如果是敏感词中的英文
			if word == "love" or word == "sex" or word == "jiangge":
				words = words.replace(word, '*'*len(word))
			# 如果是中文
			else:	
				words = words.replace(word, '*'*(len(word)/3))
			#print 'JJJ'
	print words

if __name__ == "__main__":
	words = raw_input("input what you want ")
	freedom_word2(words)
