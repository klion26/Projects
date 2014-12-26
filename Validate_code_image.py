# -*- coding: utf-8 -*-
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

_letter_case = "abcdefghjkmnpqrstuvwxy" # 小写字母，除开可能干扰的字符 i l o z
_upper_case = _letter_case.upper()
_number = ''.join(map(str, range(3, 10)))
init_chars = ''.join((_letter_case, _upper_case, _number))

def craete_validate_code(size = (120, 30)
                         , chars = init_chars
                         , img_type = "GIF"
                         , mode = "RGB"
                         , bg_color = (255, 255, 255)
                         , fg_color = (0, 0, 255)
                         , font_size = 18
                         , font_type = "Arial"
                         , length = 4
                         , draw_lines = True
                         , n_line=(1, 2)
                         , draw_points = True
                         , point_chance = 2):
    '''
    @size: 图片的大小，宽*高，默认 120*30
    @chars: 允许的字符集
    @img_type：图片格式，默认 GIF
    @mode：图片模式，默认 RGB
    @bg_color：背景色，默认白色
    @fg_color：前景色，验证码字符颜色，默认#0000ff
    @font_size：验证码字体大小
    @font_type：验证码字体
    @length：验证码字符个数
    @draw_lines：是否画干扰线
    @n_line：干扰线的条数范围
    @draw_points：是否画干扰点
    @point_chance：干扰点出现的概率
    '''
    width, height = size
    # 创建一张新的图片
    img = Image.new(mode, size, bg_color)
    # 创建画布
    draw = ImageDraw.Draw(img)

    # 生成指定长度的字符串
    def get_chars():
        return random.sample(chars, length)

    def create_lines():
        '''绘制干扰线'''
        line_num = random.randint(*n_line)

        for i in range(line_num):
            # 起点
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            # 终点
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))

    def create_points():
        '''绘制干扰点'''
        chance = min(100, max(0, int(point_chance)))

        for w in xrange(width):
            for h in xrange(height):
                tmp = random.randint(0, 100)
                if tmp>100-chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_strs():
        ''' 绘制验证码字符'''
        c_chars = get_chars()
        strs = ' %s ' % ' '.join(c_chars) # 每个字符前后以空格隔开

        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)

        draw.text(((width - font_width)/3, (height-font_height)/3),
                  strs, font=font, fill=fg_color)
        return ''.join(c_chars)

    if draw_lines:
        create_lines()
    if draw_points:
        create_points()
    strs = create_strs()

    # 图形扭曲参数
    params = [1-float(random.randint(1, 2))/100
              ,0
              ,0
              ,0
              ,1-float(random.randint(1, 10))/100
              ,float(random.randint(1, 2))/500
              ,0.001
              ,float(random.randint(1, 2))/500]
    img = img.transform(size, Image.PERSPECTIVE, params)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    return img, strs
# 生成验证码图片
def create_validate_img(size = (120, 30)
			, chars = init_chars
			, length = 4
			, img_type = "GIF"
			, draw_lines = True
			, lines = 2
			, draw_points = True
			, pro = 2):
	#@size 图片大小
	#@chars 字符集
	#@length 字符个数
	#@img_type 图片类型
	#@draw_lines 是否画线
	#@lines 画线条数
	#@draw_points 是否画点
	#@pro 画点的概率
	width, height = size
	img = Image.new("RGB", size, (255, 255, 255))
	draw = ImageDraw.Draw(img)
	# 生成验证码图片上的字符集
	def get_chars():
		return random.sample(chars, length)
	# 在验证码上进行写字操作，并返回字符集
	def create_str():
		c_str = get_chars()
		strs = ' %s ' % ' '.join(c_str)
		draw.text((width/3, height/3), strs, fill="black")
		return ''.join(c_str)

	# 在图片上进行画线
	def draw_lines():
		linecolor = (0, 0, 0)
		# 随即画线条数
		for i in xrange(random.randint(0, lines)):
			# 随即起始点
			begin = (random.randint(0, width), random.randint(0, height))
			# 随即结束点
			end = (random.randint(0, width), random.randint(0, height))
			# 画线
			draw.line([begin, end], linecolor)

	strs = create_str()
	if draw_lines:
		draw_lines()
	return img, strs
if __name__ == "__main__":
    #code_img = craete_validate_code()
	code_img, strs = create_validate_img()
	code_img.save("validate.gif", "GIF")
    
