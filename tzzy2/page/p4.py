import tkinter
import tkinter as tk
from tkinter import filedialog, ttk
from gunneng.yasuo import *
from gunneng.beifen import *
from page import zhujian


class p4:
    zi=None
    def shuru(page4):
        # 文本
        label = zhujian.zj.texts(page4, "浏览文件路径")
        label.place(anchor=tk.NW, x=9)

        # 输入路径
        suk, button= zhujian.zj.kuang(page4, "浏览路径","浏览文件路径","4")
        suk.place(anchor=tk.NW, x=10, y=25)
        button.place(anchor=tk.NW, x=225, y=25, width=70, height=20)

        # 文本
        label = zhujian.zj.texts(page4, "输出文件路径")
        label.place(anchor=tk.NW, x=9, y=50)
        # 输出路径
        suk2, button2= zhujian.zj.kuang(page4, "浏览路径","输出文件路径","4")
        suk2.place(anchor=tk.NW, x=10, y=75)
        button2.place(anchor=tk.NW, x=225, y=75, width=70, height=20)

        # 下拉框
        label = zhujian.zj.texts(page4, "选择压缩类型")
        label.place(anchor=tk.NW, x=9, y=100)
        lis = ["所有照片", "路径下照片", ".png", ".jpg"]
        select = zhujian.zj.xaila(page4, lis, "选择压缩类型", "4")
        select.place(anchor=tk.NW, x=10, y=125)

        # 命名
        label = zhujian.zj.texts(page4, "压缩比例(0-100)")
        label.place(anchor=tk.NW, x=160, y=100)

        # 按钮开始
        suzi,button= zhujian.zj.suk(page4,"开始压缩","4","压缩比")
        suzi.place(anchor=tk.NW, x=163, y=125, width=125, height=23)
        button.place(anchor=tk.NW, x=9, y=155, width=280, height=30)




def kais():
    shuru=beifen.diaoyong("浏览文件路径","4")
    shucu=beifen.diaoyong("输出文件路径","4")
    yasuobi = int(beifen.diaoyong("压缩比", "4")[0])
    print(shuru[0])
    print(shucu[0])
    print(yasuobi)
    yashuo(shuru[0]+"/",shucu[0]+"/",yasuobi)

