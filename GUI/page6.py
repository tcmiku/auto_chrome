from tkinter import ttk, filedialog
import tkinter as tk
from tkinter import *

from data.WebJsonIn import WebJsonIn_data


class Page6(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text="DNS导入模板：")
        self.label.pack()

        self.entry_file = Label(self, text="")
        self.output_file = Label(self, text="")
        self.button_file = Button(self, text="输入位置", command=self.select_file)
        self.entry_file.pack()
        self.button_file.pack(side=RIGHT)

        self.label_name = Label(self, text="输入域名:")
        self.label_name.pack()

        # 输入框
        self.selected_name = Entry(self)
        self.selected_name.pack()

        # 下拉选择框
        self.label_content = Label(self, text="选择模板内容:")
        self.label_content.pack()
        self.page_contents = ["namecheap.txt","yanximail.com.txt","域名导入模板.txt"]  # 示例页面内容
        self.selected_content = StringVar(self)
        self.selected_content.set(self.page_contents[0])  # 设置默认值
        self.dropdown_content = OptionMenu(self, self.selected_content, *self.page_contents)
        self.dropdown_content.pack()

        self.line = Label(self, text="-"*90)
        self.line.pack()

        self.button_create = Button(self, text="生成", command=self.create_page,width=15)
        self.button_create.pack()

        self.line = Label(self, text="-"*90)
        self.line.pack()


        self.line = Label(self, text="预览窗口:")
        self.line.pack()
        self.text_preview = Text(self, height=15, width=70)
        self.text_preview.pack()

    def create_page(self):
        file_name = self.selected_content.get()
        new_file_name = "./data/"+file_name
        web_name = self.selected_name.get()
        output_file = f"new_data/new_{file_name}"
        data =WebJsonIn_data(new_file_name,output_file,web_name)
        self.text_preview.delete(1.0, END)
        self.text_preview.insert(INSERT,data)

    def select_file(self):
        file_path = filedialog.askopenfilename()
        self.entry_file.config(text=file_path)