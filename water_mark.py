# -*- coding: utf-8 -*-
import Image, ImageEnhance, ImageDraw, ImageFont, ImageFilter

# img 是原图， mark 是水印图片，count 是要添加的数字
def water_mark(img, mark, count=1):
    #layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
    # 得到宽度和长度
    width, height = img.size[0], img.size[1]
    #m_width, m_height = mark.size[0], mark.size[1]
    #layer.paste(mark, (width-m_width, 0))

    #img = Image.composite(layer, img, layer)

    #在 img 上作图，即在上面添加数字水印
    draw = ImageDraw.Draw(img)
    # 生成相应字体，需要导入 _imagingft 包，暂时没有找到合适的解决方法
    #fontPath = "C:\Windows\Fonts\Arial"
    #winFont = ImageFont.truetype(fontPath, 16)
    
    # 添加数字水印，数值等于 count，颜色为红色，
    # 由于 _imagingft 包导入问题，暂时不能更改数字水印的大小
    draw.text((width-10, 0), str(count), fill='red')
    # 保存含有水印的图片
    img.save('new.png', 'PNG', quality=100)

if __name__ == "__main__":
    imgpath = raw_input("input the path of the image:")
    img = Image.open(imgpath)
    mark = Image.open(imgpath)
    water_mark(img, mark, 6)
