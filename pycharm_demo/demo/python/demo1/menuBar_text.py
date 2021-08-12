
from tkinter import *
from tkinter import messagebox
from tkColorPicker import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from  tkinter import  filedialog
from tkinter import scrolledtext
import fileinput
import os


class menuBar(object):
    def __init__(self):
        self.bgcolor = None
        # 打开的文件路径；打开的文件路径
        self.file = None
        self.f = None
        # 创建主窗口
        self.root = Tk()
        self.root.title('菜单栏')
        self.root.geometry('500x500')
        # self.fram = Tk.frame(self.root)
        # self.fram.pack()

        self.create_menu()
        self.root.mainloop()
    #创建菜单栏
    def create_menu(self):
        # 创建菜单栏
        self.menuBar = Menu(self.root)
        self.root.config(menu=self.menuBar)
        # 创建第一级菜单项fill
        self.fillBar = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='第一个菜单栏', menu=self.fillBar)
        self.twoBar = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Open', menu=self.twoBar)
        # 创建fill下面的二级菜单项
        self.fillBar.add_command(label='new', command=self.winOne)
        self.fillBar.add_separator()
        self.fillBar.add_command(label='Exit', command=self.ExitClick)

        self.twoBar.add_command(label='OpenColor', command=self.Open_Color)
        self.twoBar.add_separator()
        # accelerator 在子菜单后面追加文字
        self.twoBar.add_command(label='打开', command=self.Open_File, accelerator='Ctr + O')
        self.twoBar.bind_all("<Control-o>", self.Open_File)
        self.twoBar.add_separator()
        self.twoBar.add_command(label='保存', command=self.Save_File)
        self.twoBar.add_command(label='另存为',command=self.Saves_File)

        # 创建文本域
        self.textnew = scrolledtext.ScrolledText(self.root, fg=self.bgcolor, width=100, height=100, wrap=tk.WORD)
        # textnew.grid()
        self.textnew.pack()

    # 关闭事件
    def ExitClick(self):
        # 关闭窗口
        self.root.quit()
        # 将所有控件销毁，内存回收
        self.root.destroy()
        exit()
    # 创建子窗口
    def winOne(self):
        top1 = Toplevel()
        top1.title('子窗口')
        top1.geometry('400x300')
        but1 = Button(top1, text='子窗体按钮', command=self.help_test)
        but1.pack()
        # 取消窗口的最大化最小化按钮
        # top1.attributes('-toolwindow', 1)
        top1.focus_get()
        # 窗口顶置
        top1.wm_attributes('-topmost', 1)

    def help_test(self):
        '''
        askokcancel 确定、取消对话框,按钮返回值 True/False
        askquestion 是、否对话框，按钮返回值 yes/no
        askyesno    是、否对话框，按钮返回值 True/False
        showerror   错误对话框，按钮返回值 ok
        showinfo    按钮返回值 ok
        showwarning 警告对话框 按钮返回值 ok
        :return:
        '''
        ask = messagebox.askokcancel('点击','按钮被点击了',)
        if ask:
            print('确定',ask)
        else:
            print('取消')
    # 打开颜色控制面板
    def Open_Color(self):
        # color = askcolor('red',0,'颜色面板')
        # if color[1] != None:
        #     print('选中的颜色是：',color)
        #     self.bgcolor = color[1]
        # else:
        #     print('没有选择颜色！',color)
        color = askcolor()
        self.textnew["foreground"] = color[1]
    def Open_File(self,event=None):
        self.file = askopenfilename(filetypes=[('txt','*.txt')])
            # 给文本框赋值
        for line in fileinput.input(self.file):
            self.textnew.insert("1.0",line)

    def Save_File(self):
        # 获取文本域中的数据
        test = self.textnew.get(1.0,END)
        # print(test)
        # 判断文件是否是文件
        # if os.path.isfile(self.file):
        if self.file!=None:
            self.f = open(self.file, 'w')
            # 将文本域中修改后的值保存
            self.f.write(str(test))
            self.f.close()
        else:
            # 另存为打开文件夹
            name = filedialog.asksaveasfilename(title='保存文件', filetypes=[('保存文件','*.txt')],defaultextension='.txt')
            print('aa', name)
            if name:
                fop = open(name, 'w')
                fop.write(str(test))
                # fop.fileno()
                fop.close()
    def Saves_File(self):
        # 获取文本域中的数据
        test = self.textnew.get(1.0, END)
        # 另存为打开文件夹
        name = filedialog.asksaveasfilename(title='保存文件', filetypes=[('保存文件', '*.txt')], defaultextension='.txt')
        print('aa', name)
        if name:
            fop = open(name, 'w')
            fop.write(str(test))
            # fop.fileno()
            fop.close()
    def delete(self):
        self.textnew.insert(tk.INSERT, '')
        self.textnew.update()



menu_bar = menuBar()
