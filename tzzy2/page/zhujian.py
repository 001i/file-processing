import tkinter
import tkinter as tk
from tkinter import filedialog, ttk
from gunneng.beifen import *
from gunneng.yasuo import *
from page import p4
from page import p3
from page import p1
from tkinter import *

class zj:
    # 按钮
    # def cc():
    #     print("cccc")
    #
    # def anliu(root,mane,hanshu):
    #     anliu1=tk.Button(root,text=mane,command=hanshu)
    #     anliu1.pack(pady=10,padx=10)

    # 输入框
    def suk(root, name, zi, te):
        suk = tk.Entry(root, width=16)

        def getzi(zi, te):
            value = suk.get()
            beifen.create_text_file(name=te, text=value, shuzi=zi)
            if "1"==zi:
                p1.kais()
            # if "2"==zi:
            #     p2.kais()
            if "3"==zi:
                p3.kais()
            if "4"==zi:
                p4.kais()
            else:
                print("没有值")
        # 按钮
        button = tk.Button(root, text=name, command=lambda: getzi(zi, te))

        # suk.bind("<KeyRelease>", zj.open_directory)
        return suk, button

    # 文件夹输入框路径
    def kuang(root, te, name, zi):
        # 创建输入框
        suk = tk.Entry(root, width=29)
        # suk.place(anchor=tk.NW, x=10, y=25)
        # 创建打开文件夹按钮
        button = tk.Button(root, text=te, command=lambda: zj. open_directory(suk, name, zi))
        # button.place(anchor=tk.NW,x=225,y=25,width=70,height=20)
        # 监听输入框中的文字变化
        # suk.bind("<KeyRelease>", open_directory)
        return suk, button

    def open_directory(suk, name, zi):
        # 打开文件夹对话框
        directory = filedialog.askdirectory()
        # directory = filedialog.askopenfilename()
        # 将文件夹路径填充到输入框
        if directory:
            suk.delete(0, tk.END)  # 清空输入框中的内容
            suk.insert(0, directory)  # 将文件夹路径填充到输入框
        # # 获取输入框中的内容
        content = suk.get()+"/"
        beifen.create_text_file(name=name, text=content, shuzi=zi)
        print(content)

    # 文本
    def texts(root, te):
        label = tk.Label(root, text=te)
        return label


    def xaila(root, lis,te,zi):
        def show(event):
            value = select.get()
            print(value)
            beifen.create_text_file(name=te, text=value, shuzi=zi)
            # return value

        # 下拉框
        select = ttk.Combobox(root, width=15, textvariable=tkinter.StringVar(), state="readonly")
        # lis = ["数字", "小写字母", "大写字母", '自定义']
        # lis = ["所有照片", "路径下照片",".png",".jpg"]
        select['values'] = lis
        # select.bind("<KeyRelease>", show(te,zi))
        select.bind("<<ComboboxSelected>>",show)
        return select



