import tkinter
import tkinter as tk
from tkinter import filedialog, ttk

from gunneng.beifen import *
from page import zhujian
from gunneng.addwenjian import *
class p1:

    def shuru(page1):
        # 文本
        label=zhujian.zj.texts(page1,"需要创建文件/文件夹的位置")
        label.place(anchor=tk.NW, x=9)

        suk, button=zhujian.zj.kuang(page1,"浏览文件夹","创建文件路径记录","1")
        suk.place(anchor=tk.NW,x=10,y=25)
        button.place(anchor=tk.NW, x=225, y=25, width=70, height=20)

        label2 = zhujian.zj.texts(page1, "选择创建类型")
        label2.place(anchor=tk.NW, x=9,y=50)

        lis = ["文件夹", "文本.txt"]
        select=zhujian.zj.xaila(page1,lis,"创建类型记录","1")
        select.place(anchor=tk.NW, x=10, y=75)


        label3 = zhujian.zj.texts(page1, "创建数量")
        label3.place(anchor=tk.NW, x=160,y=50)

        suk2,button2=zhujian.zj.suk(page1,name="开始创建",te="创建数量记录",zi="1")
        suk2.place(anchor=tk.NW,x=160,y=75)
        button2.place(anchor=tk.NW, x=9, y=105, width=280, height=30)

def kais():
    lujing = beifen.diaoyong("创建文件路径记录", "1")
    shuliang = int(beifen.diaoyong("创建数量记录", "1")[0])
    # print(type(shuliang))
    laixing = beifen.diaoyong("创建类型记录", "1")

    if "文件夹"==laixing[0]:
        wenjian.addwja(path=lujing[0], shuliang=shuliang)
    if "文本.txt"==laixing[0]:
        wenjian.addwj(lujing[0],shuliang)
    else:
        print("创建类型错误")
