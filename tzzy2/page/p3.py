from gunneng import yidong
from gunneng.beifen import beifen
from gunneng.muluwenjian import mulu
from page import zhujian
import tkinter as tk


class p3:
    def shuru(page3):

        # 文本
        label = zhujian.zj.texts(page3, "浏览文件路径")
        label.place(anchor=tk.NW, x=9)

        # 输入路径
        suk, button = zhujian.zj.kuang(page3, "浏览路径", "浏览文件路径", "3")
        suk.place(anchor=tk.NW, x=10, y=25)
        button.place(anchor=tk.NW, x=225, y=25, width=70, height=20)

        # 文本
        label = zhujian.zj.texts(page3, "输出文件路径")
        label.place(anchor=tk.NW, x=9, y=50)
        # 输出路径
        suk2, button2 = zhujian.zj.kuang(page3, "浏览路径", "输出文件路径", "3")
        suk2.place(anchor=tk.NW, x=10, y=75)
        button2.place(anchor=tk.NW, x=225, y=75, width=70, height=20)

        label2 = zhujian.zj.texts(page3, "选择类型")
        label2.place(anchor=tk.NW, x=9, y=100)

        lis = ["复制", "移动"]
        select=zhujian.zj.xaila(page3,lis,"选择类型","3")
        select.place(anchor=tk.NW, x=10, y=125)

        label2 = zhujian.zj.texts(page3, "选择移动类型")
        label2.place(anchor=tk.NW, x=159, y=100)

        lis = ["文件", "文件夹","全部"]
        select = zhujian.zj.xaila(page3, lis, "选择移动类型", "3")
        select.place(anchor=tk.NW, x=160, y=125)

        # suzi, button = zhujian.zj.suk(page3, "输出移动文件文档", "3", "输出移动文件文档")
        # button.place(anchor=tk.NW, x=9, y=160, width=280, height=30)

        # 文本
        label = zhujian.zj.texts(page3, "输入移动文件文档")
        # label.place(anchor=tk.NW, x=9,y=195)
        label.place(anchor=tk.NW, x=9, y=150)

        suk3, button3 = zhujian.zj.kuang(page3, "移动文件", "输入移动文件文档", "3")
        # suk3.place(anchor=tk.NW, x=10, y=220)
        # button3.place(anchor=tk.NW, x=225, y=220, width=70, height=20)
        suk3.place(anchor=tk.NW, x=10, y=170)
        button3.place(anchor=tk.NW, x=225, y=170, width=70, height=20)

        suzi, button = zhujian.zj.suk(page3, "开始移动", "3", "开始移动文件")
        # button.place(anchor=tk.NW, x=9, y=260, width=280, height=30)
        button.place(anchor=tk.NW, x=9, y=210, width=280, height=30)
#选择类型
def leixing():
    leix =beifen.diaoyong("选择类型")
    if "复制"==leix:
        print("复制")
        return 0
    if "移动"==leix:
        print("移动")
        return 0
    else:
        print("选择类型错误")
        return 0

def yidongleix():
    yidong = beifen.diaoyong("选择移动类型")
    if "文件"==yidong:
        print("文件")
        return 0
    if "文件夹"==yidong:
        print("文件夹")
        return 0
    if "全部"==yidong:
        print("全部")
        return 0
    else:
        print("选择类型错误")
        return 0

def kais():
    shuru = beifen.diaoyong("浏览文件路径", "3")
    shucu = beifen.diaoyong("输出文件路径", "3")
    lx = beifen.diaoyong("选择类型", "3")
    # ydlx = beifen.diaoyong("选择移动类型", "3")

    shurus=shuru[0][:-1]
    # shuruss = shuru[0]
    shucus = shucu[0]
    lxs=lx[0]
    # ydlxs = lx[0]

    # suru=mulu.wj_shuliang(shuruss)
    # print(suru[0])

    # print(shurus)
    yidong.wjcz.wenjian(shurus,shucus,lxs)
    