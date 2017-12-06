import xmltodict
import tkinter.messagebox as messagebox
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
