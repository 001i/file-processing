import tkinter as tk
import openpyxl

def read_excel_data(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # 读取A1到A12的数据
    data = []
    for row in sheet.iter_rows(min_row=1, max_row=12, min_col=1, max_col=1):
        for cell in row:
            data.append(cell.value)

    return data

def open_excel_file():
    file_path = file_entry.get()
    data = read_excel_data(file_path)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, '\n'.join(str(item) for item in data))

root = tk.Tk()
root.title("读取Excel数据")

# 文件路径输入框
file_label = tk.Label(root, text="Excel文件路径：")
file_label.pack()
file_entry = tk.Entry(root, width=50)
file_entry.pack()

# 打开文件按钮
open_button = tk.Button(root, text="打开文件", command=open_excel_file)
open_button.pack()

# 结果显示框
result_label = tk.Label(root, text="读取的数据：")
result_label.pack()
result_text = tk.Text(root, width=50, height=10)
result_text.pack()

root.mainloop()
