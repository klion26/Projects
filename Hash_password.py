# -*- coding: utf-8 -*-
import hashlib, uuid
# 对密码进行加密
# password 是密码明文
# salt 是随即字符串
# algo 是不同的加密算法
def hash_password(password, salt=None, algo=0):
	# 设置 salt
	if salt is None:
		salt = uuid.uuid4().hex
	# 根据不同的 algo 调用不同的加密算法
	if algo==0:
		hash_object = hashlib.md5(password + salt)
	elif algo==1:
		hash_object = hashlib.sha1(password + salt)
	elif algo==2:
		hash_object = hashlib.sha224(password + salt)
	elif algo==3:
		hash_object = hashlib.sha256(password + salt)
	elif algo==4:
		hash_object = hashlib.sha384(password + salt)
	elif algo==5:
		hash_object = hashlib.sha514(password + salt)
	else:
		print "Algorithm you passed isn't supported"
		return None
	# 得到加密后的密文
	hex_dig = hash_object.hexdigest()
	# 把 slat 加在 password 后面，用来验证
	return hex_dig+":"+salt

if __name__ == "__main__":
	password = raw_input("input your password: ")
	hpassword = hash_password(password, None, 1)
	print hpassword
