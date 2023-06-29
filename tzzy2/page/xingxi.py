import tkinter as tk
from tkinter import ttk

class VirtualTable(tk.Frame):
    def __init__(self, master, data):
        super().__init__(master)

        self.data = data
        self.columns = ["照片名", "大小", "路径"]

        # 创建滚动条
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 创建表格
        self.treeview = ttk.Treeview(self, columns=self.columns, show="headings", yscrollcommand=self.scrollbar.set)
        self.treeview.pack(fill=tk.BOTH, expand=True)

        # 配置表格列
        for col in self.columns:
            self.treeview.heading(col, text=col)

        # 配置滚动条
        self.scrollbar.config(command=self.treeview.yview)

        # 加载数据
        self.load_data()

    def load_data(self):
        # 清空表格
        self.treeview.delete(*self.treeview.get_children())

        # 添加数据
        for item in self.data:
            self.treeview.insert("", tk.END, values=item)

def xingxi(root):
    # 创建主窗口
    # window = tk.Tk()
    # window.title("照片信息表格")
    # window.geometry("400x300")

    # 模拟大量数据
    data = [
        ["照片名1", "大小1", "路径1"],
        ["照片名2", "大小2", "路径2"],
        ["照片名3", "大小3", "路径3"],
        # 添加更多数据行...
    ]

    # 创建虚拟表格
    table = VirtualTable(root, data)
    table.pack(fill=tk.BOTH, expand=True)

    # 运行主循环
    # window.mainloop()

# if __name__ == "__main__":
#     main()
