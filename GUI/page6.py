from tkinter import ttk, filedialog
import tkinter as tk
from tkinter import *

from data.WebJsonIn import WebJsonIn_data


class Page6(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text="DNS导入模板：")
        self.label.grid(row=0, column=1, padx=1, pady=1)

        self.entry_file = Label(self, text="")
        self.output_file_name = Label(self, text="")
        self.entry_file.grid(row=1, column=0, padx=1, pady=1)
        self.output_file_name.grid(row=1, column=2, padx=1, pady=1)
        self.button_file = Button(self, text="输入位置", command=self.select_file)
        self.button_out_file = Button(self, text="输出位置", command=self.output_file)
        self.button_out_file.grid(row=2, column=2, padx=1, pady=1)
        self.button_file.grid(row=2, column=0, padx=1, pady=1)


        self.label_name = Label(self, text="输入域名:")
        self.label_name.grid(row=3, column=1, padx=1, pady=1)

        # 输入框
        self.selected_name = Entry(self)
        self.selected_name.grid(row=4, column=1, padx=1, pady=1)

        # 下拉选择框
        self.label_content = Label(self, text="选择模板内容:")
        self.label_content.grid(row=5, column=1, padx=1, pady=1)
        self.page_contents = ["namecheap.txt","yanximail.com.txt","域名导入模板.txt"]  # 示例页面内容
        self.selected_content = StringVar(self)
        self.selected_content.set(self.page_contents[0])  # 设置默认值
        self.dropdown_content = OptionMenu(self, self.selected_content, *self.page_contents)
        self.dropdown_content.grid(row=6, column=1, padx=1, pady=1)

        self.line = Label(self, text="-"*90)
        self.line.grid(row=7, column=1, padx=1, pady=1)

        self.button_create = Button(self, text="生成", command=self.create_page,width=15)
        self.button_create.grid(row=8, column=1, padx=1, pady=1)

        self.line = Label(self, text="-"*90)
        self.line.grid(row=9, column=1, padx=1, pady=1)


        self.line = Label(self, text="预览窗口:")
        self.line.grid(row=10, column=1, padx=1, pady=1)
        self.text_preview = Text(self, height=15, width=70)
        self.text_preview.grid(row=11, column=1, padx=1, pady=1)

    def create_page(self):
        file_name = self.selected_content.get()
        entry_file = self.entry_file.cget("text")
        output_file = self.output_file_name.cget("text")
        new_file_name = entry_file+"/"+file_name
        web_name = self.selected_name.get()
        output_file = output_file+f"/new_{file_name}"
        data =WebJsonIn_data(new_file_name,output_file,web_name)
        self.text_preview.delete(1.0, END)
        self.text_preview.insert(INSERT,data)

    def select_file(self):
        file_path = filedialog.askdirectory()
        self.entry_file.config(text=file_path)

    def output_file(self):
        file_path = filedialog.askdirectory()
        self.output_file_name.config(text=file_path)