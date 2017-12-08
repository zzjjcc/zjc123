import xmltodict
import tkinter.messagebox as messagebox
from tkinter import *


class gongzuoclass (object):
    def gongzuo(self='data.txt'):
        # 打开文件
        # openxml='data.txt'#+ input('data.txt')
        try:
            openxml=open(str(self),'r',encoding='UTF-8')
        except:
            name='无法找到文件位置'
            return messagebox.showinfo('警告', ' %s' % name)
            pass
        # openxml = open(data, 'r', encoding='UTF-8')
        openxml=openxml.read
        # 解析成有序dict（OrderedDict）
        xmlzhuandict = xmltodict.parse(openxml())
        # 拷贝一份备份
        xmlzhuandict2=xmlzhuandict.copy()
        #print(xmlzhuandict)
        # print(xmlzhuandict.popitme())
        xmlzhuandict2=xmlzhuandict2.pop("resources")
        xmlzhuandict2=xmlzhuandict2.pop("string")

        a=len(xmlzhuandict2)
        b=0
        f=[]
        n=0
        for b in list(range(a)):
            c=xmlzhuandict2[b]
            # namekey=c.keys()
            # print(c)
            d = ()
            for k, v in c.items():
                d=d+(v,)
                n=n+1
                # print(d, n)
            e = [d, ]
            f = f + e
        return f

    def makeform(root, lists):
        entries = []
        for field in lists:
            row = Frame(root)
            lab = Label(row, width=50, text=field, anchor='w')
            ent = Entry(row,width=50,highlightthickness=1,highlightcolor='red',takefocus=1)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((field, ent))
        print(entries)

        return entries
