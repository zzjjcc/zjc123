import xmltodict

class openxmlclss (object):

    def openxml(openfile='/Users/zjc/Documents/zjc/strings_common.xml'):
        #打开文件
        # openfile='/Users/zjc/Documents/zjc/strings_common.xml'+input('/Users/zjc/Documents/zjc/strings_common.xml')
        openfile=open(openfile,'r',encoding='utf8' )
        openfile=openfile.read()

        #转换成有序字典（OrderedDict）
        openxml=xmltodict.parse(openfile)

        #去掉外壳
        openxml=openxml.setdefault(('resources'))
        openxml=openxml.setdefault(('string'))
        # 转换成list
        a=len(openxml)
        b=range(a)
        c=()
        for i in list(b):
            d=openxml[i]
            e=()
            # print(d)
            # for k,v in d.items():
            #      print(k,v)
            for k, v in d.items():
                f=(v,)
                e=e+f
            c=(e,)+c
        return c