import random
import json

def ren_chuli(ren):
    shu_rude = str(ren)
    if shu_rude in dict1:
        return shu_rude
    elif shu_rude not in dict1.values():
        return ren_chuli(input('请重新输入:'))
    else:
        return [k for k, v in dict1.items() if v == shu_rude][0]

with open('l.txt','r') as f:
    l_txt = f


sys1 =str(random.randint(1,len(dict1)))
renshurude=ren_chuli(input('请输入：'))

print(dict1[sys1])
if sys1 == renshurude:
    jieguo = '平局'
elif sys1=='1' :
    if renshurude=='2':
        jieguo = 'huosheng'

print('电脑出的是：%s\n''你出的是  ：%s\n''结果是    ：%s\n'%(dict1[sys1],dict1[renshurude],jieguo))
