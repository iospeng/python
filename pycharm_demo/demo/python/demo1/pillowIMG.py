# -*- coding: utf-8 -*-
# !usr/bin/python

from PIL import Image,ImageFont,ImageFilter,ImageDraw
import random
# import matplotlib.pyplot as plt

# # 打开一个jpg图像文件，
# im = Image.open('D:\image\zi.png')
# # 查看图像
# # plt.figure("红色")
# # plt.imshow(im)
# # plt.show()
# # im.show()
# # 获得图片尺寸
# w,h = im.size
# print('w = %f,h = %f'%(w,h))
# # 缩放到50%
# im.thumbnail((w/2,h/2))
# print('w = %s,h = %s'%(w/2,h/2))
# # im.show()
# # 保存图片
# im.save('D:/image/zi1.png')

# 图片模糊处理
originalImage = Image.open('D:\image\hello.png')
hello = originalImage.filter(ImageFilter.BLUR)
hello.save('D:\image\hello1.png')

randomstr = chr(random.randint(65,90))
# print('随机字母：',randomstr)



# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
#创建一个颜色为白色的图片
image = Image.new('RGB', (width, height), (255, 255, 255))
# image.save('D:/image/dise.jpg')
# 创建Font对象:文字字体
font = ImageFont.truetype('C:\Windows\Fonts\msyhbd.ttf', 36)
# 创建Draw对象:把将要修改的图片对象赋值给draw，修改draw就相当于修改原图片
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        # print作用：修改目标图片颜色
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    # text参数 draw.text（坐标，文字，字体，字体颜色）
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    # print('随机字母：',rndChar())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('D:/image/code.jpg')
