import tkinter as tk
from tkinter import filedialog

def select_file():
    # 创建一个Tkinter窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 打开文件选择对话框
    file_path = filedialog.askopenfilename(title="选择一个文件")

    # 打印选择的文件路径
    if file_path:
        print("选择的文件路径:", file_path)
    else:
        print("没有选择任何文件")

if __name__ == '__main__':
    select_file()
