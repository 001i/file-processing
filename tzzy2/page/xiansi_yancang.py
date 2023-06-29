# 隐藏界面
import tkinter as tk


def show_page(page_name,pages):
    # 隐藏所有页面
    for page in pages.values():
        page.pack_forget()

    # 显示选定页面
    pages[page_name].pack()

# 调用界面
def create_page(parent, page_name, content):
    frame = tk.Frame(parent)
    label = tk.Label(frame, text=content)
    label.pack()
    return frame

