from tkinter import *
import tkinter as tk
from tkinter import ttk
from gongzuo import gongzuoclass
from tkinter.scrolledtext import ScrolledText

# var = StringVar()

# frm_ll=Scrollbar.set(frm)
# left
# var= StringVar()
# frm_L = Frame(frm)
# frm_R = Entry(frm,highlightthickness=1,highlightcolor='red',takefocus=1 )
gongzuo1=gongzuoclass.gongzuo()
listvi=[]
for i in list(range(len(gongzuo1))):
    lilinshi = [gongzuo1[i][1], ]
    listvi = listvi + lilinshi
    # Label(frm_L, text='%s'% lilinshi, font=('Arial', 15)).pack()
    # # Entry(frm, textvariable=var)
    #
    # Entry(frm_L, textvariable=var)
    # var.set(lilinshi)
    # frm_L.pack(side=LEFT)
    # frm_R.pack(side=RIGHT)
    # frm.pack()
    # right
    # Label(frm_R, text='%s'% i, font=('Arial', 15)).pack(side=TOP)


if __name__ == '__main__':
    root = Tk()
    # 添加标题
    root.title("翻译")
    root.geometry('600x600')
    frm=Frame(root)
    frml = Frame(frm)


    ents = gongzuoclass.makeform(frml, listvi)
    frml.pack(side=LEFT, fill=Y)

    scrollbar1 = Scrollbar(frm)
    scrollbar1.pack(side=RIGHT, fill=Y)

    scrollbar1.config(command=frml.yview,width=20, height=20, background='#ffffff')


    frm.pack(fill=Y)
    root.mainloop()
