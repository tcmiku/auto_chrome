from tkinter import ttk
import tkinter as tk
from tkinter import *

class Page5(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label0 = Label(self, text="PPFunnel 插件文本")
        self.label0.grid(row=0, column=0)

        # 创建 Label 组件
        self.label = tk.Label(self, text="这是一个可以复制的文本。")
        self.label.grid(row=1, column=0, padx=10, pady=10)

        # 创建右键菜单
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="复制", command=self.copy_to_clipboard)

        # 绑定右键点击事件
        self.label.bind("<Button-3>", self.show_context_menu)

    def copy_to_clipboard(self,event=None):
        # 获取 Label 中的文本
        text = self.label.cget("text")
        # 将文本复制到剪贴板
        self.clipboard_clear()  # 清空剪贴板
        self.clipboard_append(text)  # 追加文本到剪贴板
        self.update()  # 更新剪贴板内容

    def show_context_menu(self,event):
        # 显示右键菜单
        self.context_menu.post(event.x_root, event.y_root)
