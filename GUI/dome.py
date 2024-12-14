import tkinter as tk
from tkinter import messagebox

def on_custom_button():
    messagebox.showinfo("提示", "自定义按钮被点击")

def close_window():
    root.destroy()

# 创建主窗口
root = tk.Tk()
root.title("自定义标题栏示例")
root.geometry("400x300")

# 创建自定义标题栏
title_bar = tk.Frame(root, bg='lightgray', relief='raised', bd=2)
title_bar.pack(fill=tk.X)

# 创建自定义按钮
custom_button = tk.Button(title_bar, text="自定义按钮", command=on_custom_button)
custom_button.pack(side=tk.LEFT, padx=5, pady=5)

# 创建关闭按钮
close_button = tk.Button(title_bar, text="关闭", command=close_window)
close_button.pack(side=tk.RIGHT, padx=5, pady=5)

# 创建标签以填充窗口的内容
content_frame = tk.Frame(root)
content_frame.pack(expand=True, fill=tk.BOTH)

label = tk.Label(content_frame, text="欢迎使用自定义标题栏示例")
label.pack(pady=20)

# 运行主循环
root.mainloop()
