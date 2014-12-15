# -*- coding: utf-8 -*-
import Image, os
# 将 dir 目录下的所有图片进行 resize
# resize 之后的大小为  w*h，w-->宽   h-->高
# 暂时只能处理文件夹内只有图片的情况，以后可以更改为
# 任意文件夹，只处理其中的图片文件
def resize_image(dir, w, h):
    #遍历文件夹内的所有文件
    for i in os.listdir(dir):
        if os.path.isfile(i):
            print i
            # 打开对应的文件
            image = Image.open(dir+"\\"+i)
            # 将文件进行 resize 处理
            image = image.resize((w,h))
            # 保存文件
            image.save(dir+"\\"+"after"+i)


if __name__ == "__main__":
    resize_image("E:\images\chessboards", 320, 120)
