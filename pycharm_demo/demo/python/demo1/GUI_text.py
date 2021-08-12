# -*- coding: utf-8 -*-
# !usr/bin/python

from tkinter import *
from tkinter import messagebox
# import phoenix
from selenium.webdriver.common.action_chains import ActionChains


# 按钮点击事件
ae = 0
def callback():
    # print('弹出式对话框')
    # messagebox.showerror('python command','python,点击事件')
    global ae
    if  ae == 0:
        butClick.configure(text='按钮以被点击',fg ='red')
        ae = 1
    else:
        butClick.configure(text='请点击',fg = '#FF8C00')
        ae = 0
    print(ae)

# 创建GUI主窗体
root = Tk()
# 主窗体标题
root.title('Button Test')
# 设置主窗体初始大小
root.geometry("500x200")
# 设置主窗体最大尺寸
# root.maxsize(600,400)
# 设置主窗体最小尺寸
# root.minsize(300,200)
# 设置主窗体透明
root.attributes('-alpha',1)
# 设置主窗体颜色
root['bg'] = '#ffffff'
# 创建画布
# canvas = Canvas(root,width = 200,height = 100,bg = 'blue')
canvas = Canvas(root, width = 300, height = 100, bg = "#FFEFD5")
# canvas.attributes('-alpha',0.7)
# fram = Frame(width = 500,height = 500)
# 将root窗口设置为这个框架的父窗口
fram = Frame(root)
# 设置位置在左上角，左边距10，右边距30
# fram.grid(sticky = 'nw',padx = 10,pady = 30)

# 在画布上画图
canvas.create_line(10,30,100,50,fill = 'red',tags = 'line')

def draw_rect():
    # 画矩形，前两个坐标表示左上角点的坐标，后两个坐标表示右下角点的坐标
    canvas.create_rectangle(10, 10, 190, 90, tags='rect')
def draw_oval():
    # 在矩形中填充椭圆形颜色
    canvas.create_oval(10, 10, 190, 90, fill='red', tags='oval')
def draw_arc():
    # 画扇形，start是开始度数，extent是结束度数
    # （度数以12点方向为0度，逆时针增长）
    # width是边框的宽度，fill扇形的颜色
    canvas.create_arc(10, 10, 190, 90, start=0, extent=90, width=2, fill='blue', tags='arc')
def draw_polygon():
    # 画多边形(两个数字为一个点坐标)画几边形，就写几个坐标
    canvas.create_polygon(10, 10, 190, 90, 150, 80, 10, 90, fill='#ffffff', tags='polygon')
def draw_line():
    # 画直线
    canvas.create_line(10, 10, 190, 90, width=3, fill='black', tags='line')
    canvas.create_line(10, 90, 190, 10, width=3, fill='black', tags='line')
def draw_text():
    # 在画布上添加文字（font可以设置文字样式）
    canvas.create_text(50, 50, text='画布已删除', font="time 10 bold underline", tags='string')
def delete_all():
    # 清空画布
    canvas.delete('rect', 'oval', 'arc', 'polygon', 'line', 'string')


# bitmap = 'gray50'属性可以使用像素精确控制按钮大小
butRect = Button(fram,text = 'drawRect',relief = 'sunken',bg = "red",command = draw_rect)
butClick = Button(fram,text = "hahah请点击",font=('Arial',12),fg = '#FF8C00',bd=2,relief=GROOVE,command = callback)
butOval = Button(fram,text = 'drawOval',compound = "right",bitmap = 'error',command = draw_oval)
butArc = Button(fram,text = 'drawArc',anchor = 'w',command = draw_arc)
butPolygon = Button(fram,text = 'drawPolygon',command = draw_polygon)
butLine = Button(fram,text = 'drawLine',command = draw_line)
butText = Button(fram,text = 'drawText',command = draw_text)
butDelect = Button(fram,text = 'Delect',command = delete_all)



# 将按钮放入主程序,并设置按钮位置
# butColor.pack()
# canvas.pack()
# butColor.pack()
# butClick.pack()
# butClick.pack()
fram.pack()
canvas.pack()

butRect.grid(row = 1,column = 1)
butClick.grid(row = 1,column = 2)
butOval.grid(row = 1,column = 3)
butArc.grid(row = 1,column = 4)
butPolygon.grid(row = 2,column = 1)
butLine.grid(row = 2,column = 2)
butText.grid(row = 2,column = 3)
butDelect.grid(row = 2,column = 4)

# 启动程序
root.mainloop()
