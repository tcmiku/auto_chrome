import threading
from tkinter import ttk
import tkinter as tk
from tkinter import *
import time

from config import run_auto


class Page4(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text="浏览器操作工具：")
        self.label.pack()

        self.chrome_id = Label(self, text="Chrome浏览器ID:")
        self.chrome_id.pack()
        self.chrome_id_entry = Entry(self)
        self.chrome_id_entry.pack()

        self.domain_name = Label(self, text="域名:")
        self.domain_name.pack()
        self.domain_name_entry = Entry(self)
        self.domain_name_entry.pack()

        # 下拉选择框
        self.label_content = Label(self, text="选择模板内容:")
        self.label_content.pack()
        self.page_contents = ["us","de","swansumo","grunsguru","grunsify"]  # 示例页面内容
        self.selected_content = StringVar(self)
        self.selected_content.set(self.page_contents[0])  # 设置默认值
        self.dropdown_content = OptionMenu(self, self.selected_content, *self.page_contents)
        self.dropdown_content.pack()

        self.line = Label(self, text="----------------------------------------------")
        self.line.pack()
        self.button_create = Button(self, text="RUN", command=self.create_page,width=15)
        self.button_create.pack()

        self.line = Label(self, text="----------------------------------------------")
        self.line.pack()

        # 添加Text组件用于显示信息
        self.text_output = Text(self, height=10, width=50)
        self.text_output.pack()


    def log(self, message):
        self.text_output.insert(tk.END, message + '\n')
        self.text_output.see(tk.END)  # 滚动到文本的最后一行

    def create_page(self):
        self.url = "http://local.adspower.com:50325"
        self.page_name = self.domain_name_entry.get()
        self.chrome_id = self.chrome_id_entry.get()
        self.content = self.selected_content.get()
        thread1 = threading.Thread(target=self.page_content)
        if self.page_name and self.chrome_id and self.content is not None:
            self.log("开始执行...")  # 打印信息到Text组件
            thread1.start()
        else:
            self.log("请填写完整信息")

    def page_content(self):
        self.log("正在执行页面内容...")
        start_time = time.time()
        try:
            run_auto(self.url,self.chrome_id,self.page_name,self.content).auto()
        except Exception as e:
            self.log(f"执行失败: {e}")
        else:
            self.log("执行成功")
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.log(f"程序运行时间: {elapsed_time:.2f} 秒")
