import tkinter as tk
from tkinter import ttk

from page.windos import center_window


class p2:
    def shuru(page2):
        selected_options = []
        selected_options_order = []

        def update_selected_options(option, var):
            if var.get():
                selected_options.append(option)
                selected_options_order.append(option)
            else:
                selected_options.remove(option)
                selected_options_order.remove(option)
            update_display()

        def update_display():
            display.delete(1.0, tk.END)
            for index, option in enumerate(selected_options_order, start=1):
                display.insert(tk.END, f"{index}: {option}\n")

        def run_selected_options():
            win = tk.Tk()
            win.title('重命名')
            width = 305
            height = 550
            center_window(win, width, height - 50)
            for option in selected_options_order:
                # 在这里根据选项执行相应的操作
                print(f"运行操作: {option}")


        # 选项列表
        # options = ["选项" + str(i) for i in range(1, 11)]
        options = ["前缀","后缀","插入","时间","数字","字母"]

        # 创建显示框
        display = tk.Text(page2, width=40, height=10)
        display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # 创建多选框并添加到界面
        checkboxes = []
        checkbox_vars = []
        row = 1
        column = 0
        for option in options:
            var = tk.BooleanVar()
            checkbox = ttk.Checkbutton(page2, text=option, variable=var,
                                       command=lambda opt=option, v=var: update_selected_options(opt, v))
            checkbox.grid(row=row, column=column, sticky="w", padx=10, pady=5)
            checkboxes.append(checkbox)
            checkbox_vars.append(var)
            column += 1
            if column == 2:
                column = 0
                row += 1

        # 创建按钮，点击时按照点击顺序运行选中的选项
        button = tk.Button(page2, text="运行选中的选项", command=run_selected_options)
        button.grid(row=row, column=0, columnspan=2, padx=10, pady=10)


