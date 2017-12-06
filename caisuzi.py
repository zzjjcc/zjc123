from gongzuo import gongzuoclass
from tkinter import *           # 导入 Tkinter 库
# http://www.cnblogs.com/kaituorensheng/p/3287652.html
# http://zetcode.com/gui/tkinter/
# http://xmsay.com/python%E5%9B%BE%E5%BD%A2%E5%B7%A5%E5%85%B7%E5%8C%85tkinter%E4%B8%AD%E5%A6%82%E4%BD%95%E8%B0%83%E6%95%B4%E5%85%83%E4%BB%B6%E5%9C%A8%E7%AA%97%E5%8F%A3%E4%BD%8D%E7%BD%AE/
# http://blog.csdn.net/lw_zhaoritian/article/details/51967529
gongzuo1=gongzuoclass.gongzuo()
lackey = []
listvi = []
for i in list(range(len(gongzuo1))):
    # print(type(i))
    lilinshi = [gongzuo1[i][1], ]
    lilinshiy = [gongzuo1[i][0], ]
    lackey = lackey + lilinshiy
    listvi = listvi + lilinshi
print(lackey,'/n',listvi)
# 创建窗口对象的背景色
root = Tk()
root.title('翻译')
root.geometry('800x600')
root.resizable(width=False, height=True)
# 创建两个列表
li     = lackey
movie  = listvi
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

frm = Frame(root)

listb.pack(side=LEFT)                    # 将小部件放置到主窗口中
listb2.pack(side=RIGHT)


root.mainloop()                 # 进入消息循环