from page.xiansi_yancang import *
from page.windos import *
from page.p1 import *
from page.p2 import *
from page.p3 import *
from page.p4 import *
from page.xingxi import *


def main():
    # 这里是主程序的逻辑
    root = tk.Tk()

    root.title('快处理')
    # 设置窗口尺寸
    width = 305
    height = 550
    # 将窗口放置在屏幕中央
    center_window(root, width, height)

    def xiaojiemian(name, text):
        win = tk.Tk()
        win.title(name)
        width = 355
        height = 200
        center_window(win, width, height)
        label = tk.Label(win, text=text)
        label.pack()
        # 运行主事件循环
        win.mainloop()

    # 创建菜单栏
    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Page 1", command=lambda: show_page('page1', pages))
    file_menu.add_command(label="Page 2", command=lambda: show_page('page2', pages))
    file_menu.add_separator()
    file_menu.add_command(label="退出", command=root.quit)
    menubar.add_cascade(label="文件", menu=file_menu)
    root.config(menu=menubar)

    guanyu = tk.Menu(menubar, tearoff=0)
    guanyu.add_command(label="帮助", command=lambda: xiaojiemian(name="帮助", text="https://github.com/001i"))
    # guanyu.add_command(label="窗口", command=lambda: show_page('page2',pages))
    guanyu.add_command(label="作者", command=lambda: xiaojiemian(name="作者", text="作者:001i"))
    guanyu.add_command(label="版本", command=lambda: xiaojiemian(name="版本",text="版本为1.0   此版本为毕设初版    阉割版    其他版本等待上线"))
    menubar.add_cascade(label="关于", menu=guanyu)
    root.config(menu=menubar)

    notebook = ttk.Notebook(root)
    notebook.pack()

    # 创建页面
    page1 = ttk.Frame(notebook, width=120, height=600)
    notebook.add(page1, text="批量创建")
    page2 = ttk.Frame(notebook)
    notebook.add(page2, text="批量命名")
    page3 = ttk.Frame(notebook)
    notebook.add(page3, text="批量移动")
    page4 = ttk.Frame(notebook)
    notebook.add(page4, text="批量压缩")
    # page5 = ttk.Frame(notebook)
    # notebook.add(page5, text="还原")
    # page6 = ttk.Frame(notebook)
    # notebook.add(page6, text="自定义")

    beifen()

    p1.shuru(page1)
    p2.shuru(page2)
    p3.shuru(page3)
    p4.shuru(page4)
    # p5.shuru(page5)

    # xingxi(root)

    # 创建页面
    pages = {}
    pages['page1'] = create_page(root, 'page1', '这是第一页')
    pages['page2'] = create_page(root, 'page2', '这是第二页')
    # pages['page3'] = create_page(win, 'page2', '这是第二页')

    # 默认显示第一页
    show_page('page1', pages)

    root.mainloop()


if __name__ == "__main__":
    # 当脚本作为主程序运行时，执行 main() 函数
    main()
