from tkinter import ttk
import tkinter as tk
from tkinter import *

from tkinter import filedialog

from new_page import NewPage


class Page1(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label_file = Label(self, text="选择模板文件位置:")

        self.entry_file = Label(self, text="")

        self.button_file = Button(self, text="选择文件", command=self.select_file)
        self.entry_file.pack()
        self.button_file.pack(side=RIGHT)
        self.label_file.pack(side=RIGHT)

        self.index = 0

        self.label = Label(self, text="页面内容生成器：")
        self.label.pack()

        self.label_name = Label(self, text="输入域名:")
        self.label_name.pack()

        # 输入框
        self.selected_name = Entry(self)
        self.selected_name.pack()

        self.label_end = Label(self, text="输入网址后缀:")
        self.label_end.pack()

        self.selected_end = Entry(self)
        self.selected_end.pack()

        self.selected_end.insert(0, "com")

        self.line = Label(self, text="-"*50)

        # 下拉选择框
        self.label_content = Label(self, text="选择模板内容:")
        self.label_content.pack()
        self.page_contents = ["us","de","swansumo","grunsguru","grunsify"]  # 示例页面内容
        self.selected_content = StringVar(self)
        self.selected_content.set(self.page_contents[0])  # 设置默认值
        self.dropdown_content = OptionMenu(self, self.selected_content, *self.page_contents)
        self.dropdown_content.pack()

        #分界线
        self.line = Label(self, text="-----------------------------------------")
        self.line.pack()
        # 创建按钮
        self.button_create = Button(self, text="生成", command=self.create_page)
        self.button_create.pack()

        self.line = Label(self, text="-----------------------------------------")
        self.line.pack()

        self.label_title = Label(self, text="网页标题:")
        self.label_title.pack()
        self.text_title = Text(self, height=1, width=50)
        self.text_title.pack()

        self.button_next = Button(self, text="下一页", command=self.next_page,width=15)
        self.button_next.pack(side=RIGHT)
        self.button_back = Button(self, text="上一页", command=self.back_page,width=15)
        self.button_back.pack(side=LEFT)

        self.label_content = Label(self, text="网页内容:")
        self.label_content.pack()
        self.text_content = Text(self, height=10, width=60)
        self.text_content.pack()

        self.button_copy = Button(self, text="复制", command=self.copy_content)
        self.button_copy.pack()

    def create_page(self):
        self.index = 0
        self.title_list = []
        self.content_list = []
        page_name = self.selected_name.get()
        page_content = self.selected_content.get()
        page_end = self.selected_end.get()
        file_path = self.entry_file.cget("text")
        print(file_path)
        new_page = NewPage(file_path,page_content)
        page_data =new_page.add_page(page_name,page_end)
        self.text_title.delete(1.0, END)
        self.text_content.delete(1.0, END)
        for i in range(len(page_data)):
            self.title_list.append(page_data["page"+str(i+1)]["title"])
            self.content_list.append(page_data["page"+str(i+1)]["content"])

        self.text_title.insert(INSERT,self.title_list[self.index])
        self.text_content.insert(INSERT,self.content_list[self.index])


    def next_page(self):
        if self.index < len(self.title_list)-1:
            self.text_title.delete(1.0, END)
            self.text_content.delete(1.0, END)
            self.index += 1
            self.text_title.insert(INSERT,self.title_list[self.index])
            self.text_content.insert(INSERT,self.content_list[self.index])

    def back_page(self):
        if self.index > 0:
            self.text_title.delete(1.0, END)
            self.text_content.delete(1.0, END)
            self.index -= 1
            self.text_title.insert(INSERT,self.title_list[self.index])
            self.text_content.insert(INSERT,self.content_list[self.index])

    def copy_content(self):
        self.text_content.get(1.0, END)
        self.text_content.clipboard_clear()
        self.text_content.clipboard_append(self.text_content.get(1.0, END))

    def select_file(self):
        file_path = filedialog.askopenfilename()
        self.entry_file.config(text=file_path)

