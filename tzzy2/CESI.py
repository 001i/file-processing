import tkinter as tk
from tkinter import filedialog
import shutil

def select_source():
    source_path = filedialog.askdirectory()  # 选择文件夹对话框
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_path)

def select_destination():
    dest_path = filedialog.askdirectory()  # 选择文件夹对话框
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, dest_path)

def move_files():
    source_path = source_entry.get()
    dest_path = dest_entry.get()

    try:
        shutil.move(source_path, dest_path)
        print("移动文件成功！")
    except FileNotFoundError:
        print("源文件或目标文件夹不存在！")
    except shutil.Error as e:
        print("移动文件时出错:", str(e))

# 创建主窗口
root = tk.Tk()

# 创建选择源文件/文件夹按钮和输入框
source_button = tk.Button(root, text="选择源文件/文件夹", command=select_source)
source_button.pack()

source_entry = tk.Entry(root)
source_entry.pack()

# 创建选择目标文件夹按钮和输入框
dest_button = tk.Button(root, text="选择目标文件夹", command=select_destination)
dest_button.pack()

dest_entry = tk.Entry(root)
dest_entry.pack()

# 创建执行按钮
execute_button = tk.Button(root, text="移动文件", command=move_files)
execute_button.pack()

# 运行主事件循环
root.mainloop()
