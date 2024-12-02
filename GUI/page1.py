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
        self.entry_file.grid(row=0, column=1, padx=1, pady=1)
        self.button_file.grid(row=1, column=1, padx=1, pady=1)
        self.label_file.grid(row=1, column=0, padx=1, pady=1)

        self.index = 0

        self.label = Label(self, text="页面内容生成器：")
        self.label.grid(row=2, column=1, padx=1, pady=1)

        self.label_name = Label(self, text="输入域名:")
        self.label_name.grid(row=3, column=0, padx=1, pady=1)

        # 输入框
        self.selected_name = Entry(self)
        self.selected_name.grid(row=3, column=1, padx=1, pady=1)

        self.label_end = Label(self, text="输入网址后缀:")
        self.label_end.grid(row=4, column=0, padx=1, pady=1)

        self.selected_end = Entry(self)
        self.selected_end.grid(row=4, column=1, padx=1, pady=1)

        self.selected_end.insert(0, "com")

        self.line = Label(self, text="-"*50)

        # 下拉选择框
        self.label_content = Label(self, text="选择模板内容:")
        self.label_content.grid(row=5, column=0, padx=1, pady=1)
        self.page_contents = ["us","de","swansumo","grunsguru","grunsify"]  # 示例页面内容
        self.selected_content = StringVar(self)
        self.selected_content.set(self.page_contents[0])  # 设置默认值
        self.dropdown_content = OptionMenu(self, self.selected_content, *self.page_contents)
        self.dropdown_content.grid(row=5, column=1, padx=1, pady=1)

        self.label_content1 = Label(self, text="是否需要手机号:")
        self.label_content1.grid(row=6, column=0, padx=1, pady=1)
        self.page_contents1 = ["phone","nophone"]  # 示例页面内容
        self.selected_content1 = StringVar(self)
        self.selected_content1.set(self.page_contents1[0])  # 设置默认值
        self.dropdown_content1 = OptionMenu(self, self.selected_content1, *self.page_contents1)
        self.dropdown_content1.grid(row=6, column=1, padx=1, pady=1)

        self.label_content2 = Label(self, text="选择内容:")
        self.label_content2.grid(row=7, column=0, padx=1, pady=1)
        self.page_contents2 = ["明浪英语","明浪德语","大冲专用","南昌专用"]  # 示例页面内容
        self.selected_content2 = StringVar(self)
        self.selected_content2.set(self.page_contents2[0])  # 设置默认值
        self.dropdown_content2 = OptionMenu(self, self.selected_content2, *self.page_contents2)
        self.dropdown_content2.grid(row=7, column=1, padx=1, pady=1)

        #分界线
        self.line = Label(self, text="-----------------------------------------")
        self.line.grid(row=8, column=1, padx=1, pady=1)
        # 创建按钮
        self.button_create = Button(self, text="生成", command=self.create_page)
        self.button_create.grid(row=9, column=1, padx=1, pady=1)

        self.line = Label(self, text="-----------------------------------------")
        self.line.grid(row=10, column=1, padx=1, pady=1)

        self.label_title = Label(self, text="网页标题:")
        self.label_title.grid(row=11, column=1, padx=1, pady=1)
        self.text_title = Text(self, height=1, width=50)
        self.text_title.grid(row=12, column=1, padx=1, pady=1)

        self.button_next = Button(self, text="下一页", command=self.next_page,width=15)
        self.button_next.grid(row=13, column=2, padx=1, pady=1)
        self.button_back = Button(self, text="上一页", command=self.back_page,width=15)
        self.button_back.grid(row=13, column=0, padx=1, pady=1)

        self.label_content = Label(self, text="网页内容:")
        self.label_content.grid(row=14, column=1, padx=1, pady=1)
        self.text_content = Text(self, height=10, width=60)
        self.text_content.grid(row=14, column=1, padx=1, pady=1)

        self.button_copy = Button(self, text="复制", command=self.copy_content)
        self.button_copy.grid(row=15, column=1, padx=1, pady=1)

        # 创建右键菜单
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="复制", command=self.copy_to_clipboard)

        # 绑定右键点击事件
        self.text_title.bind("<Button-3>", self.show_context_menu)

    def copy_to_clipboard(self, event=None):
        # 获取 Label 中的文本
        text = self.text_title.get(1.0, END)
        # 将文本复制到剪贴板
        self.clipboard_clear()  # 清空剪贴板
        self.clipboard_append(text)  # 追加文本到剪贴板
        self.update()  # 更新剪贴板内容

    def show_context_menu(self, event):
        # 显示右键菜单
        self.context_menu.post(event.x_root, event.y_root)

    def create_page(self):
        self.index = 0
        self.title_list = []
        self.content_list = []
        page_name = self.selected_name.get()
        page_content = self.selected_content.get()
        page_end = self.selected_end.get()
        file_path = self.entry_file.cget("text")
        page_phone = self.selected_content1.get()
        page_phone_content = self.selected_content2.get()
        page_list = [page_phone,page_phone_content]
        print(file_path)
        new_page = NewPage(file_path,page_content)
        page_data =new_page.add_page(page_name,page_end,page_list)
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

