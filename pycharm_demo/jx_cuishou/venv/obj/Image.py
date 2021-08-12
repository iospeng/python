# -*- coding:utf-8 -*-
import time,datetime
from PIL import ImageGrab
class Images(object):

    '''
        text1:成功文案
        text2:失败文案
        content1:获取控件中的文案
        content2:对比文案
    '''
    def get_img(self,text1,text2,content1,content2):
        time.sleep(2)
        self.text1 = text1
        self.text2 = text2
        self.content1 = content1
        self.content2 = content2
        if self.content1 == self.content2:
            print(self.text1 + self.content1)
        else:
            print(self.text2 + self.content1)
            # 图片名称拼接
            img_name = str(time.time()) + '.jpg'
            # img_name = datetime.datetime.now().strftime("%Y--%m--%d %H:%M:%S")
            path = r"D:\\install\\bg\\img\\" + img_name
            # grab(x,y,x,y) 设置截屏区域 无参截全屏
            img = ImageGrab.grab()
            print("路径为：" + path)
            # 从粘贴板复制图片
            # clip = ImageGrab.grabclipboard()
            if (img != None):
                # 保存
                img.save(path)