# -*- coding: utf-8 -*-

import urllib, re
# 从指定网址得到其中所有的图片 url
# 参数 pageurl 是指定的网址
# 返回一个 list，包含所有的图片 url
def find_image_url(pageurl):
    # 打开指定的网址
    url = urllib.urlopen(pageurl)
    # 读取指定网址 html 源文件
    contents = url.read()
    # 指定图片正则表达式规则，这里只考虑 jpg 图片，如果有其他类型的图片，需要修改正则表达式规则
    imgre = re.compile("src=\"http[^\"]*jpg\"")
    # 找到所有符合上述指定正则表达式规则的链接
    images = re.findall(imgre, contents)
    # 将所有 url 中前面的 "src=http" 以及 后面的 " 去掉
    images = [image[5:-1] for image in images]
    #for image in images:
        
    # 调用
    #save_image(images)
    # 返回所有图片链接的集合
    return images

# 根据链接保存相应图片
# 参数 images 是所有图片的链接集合，list 类型
def save_image(images):
    # 保存名字从 1.jpg 一直增大，后期可以考虑从图片链接中截取名字
    name = 1
    # 查找所有的图片
    for image in images:
        # 把图片从服务器拷贝到本机上
        urllib.urlretrieve(image, "image"+"\\"+str(name)+".jpg")
        # 名字自动加1
        name += 1
        #print image
        
if __name__ == "__main__":
    save_image(find_image_url("http://tieba.baidu.com/p/2166231880"))
