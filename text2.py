from tkinter import *
from gongzuo import gongzuoclass

def data(textList):
    for i in range(len(textList)):
        Label(frame,text=i,anchor='w').grid(row=i,column=0)
        Label(frame,text=textList[i],anchor='w').grid(row=i,column=1)
        Entry(frame,width=50,highlightthickness=1,highlightcolor='red',takefocus=1).grid(row=i, column=2)


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

root=Tk()
sizex = 1024
sizey = 600
posx  = 100
posy  = 100
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
gongzuo1=gongzuoclass.gongzuo()
listvi=[]
for i in list(range(len(gongzuo1))):
    lilinshi = [gongzuo1[i][1], ]
    listvi = listvi + lilinshi
myframe=Frame(root,relief=GROOVE,width=200,height=200,bd=1)
myframe.place(x=10,y=10)

canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
data(listvi)


root.mainloop()