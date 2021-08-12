# -*- coding: utf-8 -*-
# !usr/bin/python

from tkinter import *

class draw:
    def __init__(self):
        self.textList = []
        # 创建主窗体
        self.root = Tk()
        self.fram = Frame(self.root)
        # 创建画布
        self.canvas = Canvas(self.root, width=500, height=500, bg='#FFEFD5')

    # 按钮点击事件
    def Click(self):
        # global HOne, HTwo, HThree, ZOne, ZTwo, ZThree
        # global HOne
        lists = []
        for i in range(len(self.textList)):
            HOne = int(self.textList[i].get())
            lists.append(HOne)
            print(HOne)
        print(lists)
        for z in range(2):
            print(z)
            self.canvas.create_line(lists[z], lists[z+3], lists[z+1], lists[z+1+3], width=2, fill='blue', tags='line')
    #画控件
    def draw_control(self):
        self.root.title('折线图')
        self.fram.pack()
        # 画横纵轴
        self.canvas.create_line(3, 0, 3, 500, width=2, fill='black')
        self.canvas.create_line(0, 500, 500, 500, width=2, fill='black')
        # 横坐标上花点
        for x in range(int(500 / 50)):
            if x == 0:
                self.canvas.create_line(x * 50 + 3, 500, x * 50 + 3, 495, width=2, fill='red')
            else:
                self.canvas.create_line(x * 50, 500, x * 50, 495, width=2, fill='red')

        for y in range(int(500 / 50)):
            if y == 0:
                self.canvas.create_line(0, y * 50 + 4, 7, y * 50 + 4, width=2, fill='red')
            else:
                self.canvas.create_line(0, y * 50, 7, y * 50, width=2, fill='red')
        # 文本框属性 前提highlightthickness（文本框边框亮度）必须有值
        # highlightbackgroun(文本框未获得焦点时的颜色)
        # highlightcolor（文本框获得焦点时的颜色）
        # insertborderwidth(文本框光标宽度，有问题，待定)
        # state限制文本框是否可以操作（disabled：不可操作；normal：可操作）
        # delete方法,如：delete（10）删除索引为10的值；delete（0,10）删除索引从0到10的元素；delete（0，END）删除所有值
        for i in range(6):
            textHOne = Entry(self.fram, foreground='red', width=4, highlightbackgroun='black', highlightcolor='red',
                             highlightthickness=1, insertborderwidth=1, state='normal')
            self.textList.append(textHOne)
        butEnt = Button(self.fram, text='确定', width=10, command=self.Click)
        labOne = Label(self.fram, text='横坐标')
        labTwo = Label(self.fram, text='纵坐标')

        # 将控件放在住窗体上
        self.canvas.pack()
        labOne.grid(pady=10, row=1, column=1)
        labTwo.grid(pady=10, row=1, column=2)
        for i in range(len(self.textList)):
            if i <= 2:
                self.textList[i].grid(pady=10, row=i + 2, column=1)
            else:
                self.textList[i].grid(pady=10, row=i - 1, column=2)
        butEnt.grid(pady=10, row=5, column=1)

        self.root.mainloop()

# 初始化类对象
draw = draw()
# 类方法调用
draw.draw_control()