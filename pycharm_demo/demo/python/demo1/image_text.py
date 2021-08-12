# -*- coding: utf-8 -*-
# !usr/bin/python

from PIL import ImageFont,Image,ImageDraw

# 打开一张图片

# while 1:
#     imageAddress = input()
#     def re():
#         try:
#             images = Image.open(imageAddress)
#         except:
#             print('打开文件失败，请输入正确的文件路径！')
#             # raise SystemExit
#             return 'no'
#
#     if imageAddress == 1:

# imageAddress = 'D:\image\hello.png'
print('请输入图片地址：')
imageAddress = input()
print('请输入横坐标：')

x = int(input())
print('请输入纵坐标：')
y = int(input())
print(type(x))
print('请输入文字：')
imageTxt = input()
print('请输入文字三原色第一位：')
red1 = int(input())
print('请输入文字三原色第二位：')
yellow2 = int(input())
print('请输入文字三原色第三位：')
blue3 = int(input())

# 打开图片，打开失败就结束程序
try:
    images = Image.open(imageAddress)
except:
    print('打开文件失败，请输入正确的文件路径！')
    raise SystemExit
# 选择文字字体路径
font = ImageFont.truetype('C:\Windows\Fonts\msyhbd.ttf',25)
# 将拿到的图片赋值给draw对象，修改draw就是修改原图片
draw = ImageDraw.Draw(images)
# 设置图片的文字，文字颜色，字体
draw.text((x,y),imageTxt,font=font,fill=(250,15,85))
# 保存图片
images.save('D:/image/img.jpg')
