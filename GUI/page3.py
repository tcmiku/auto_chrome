from tkinter import ttk
import tkinter as tk
from tkinter import *
from name import Name

class Page3(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text="虚拟信息生成器：")
        self.label.pack()

        self.label_name = Label(self, text="姓名:")
        self.label_name.pack()

        self.selected_name = Entry(self)
        self.selected_name.pack()

        self.label_email = Label(self, text="邮箱:")
        self.label_email.pack()

        self.selected_email = Entry(self)
        self.selected_email.pack()

        self.label_address = Label(self, text="地址:")
        self.label_address.pack()

        self.selected_address = Entry(self)
        self.selected_address.pack()

        self.line = Label(self, text="----------------------------------------")
        self.line.pack()

        self.button_generate = Button(self, text="生成", command=self.generate_info)
        self.button_generate.pack()

    def generate_info(self):
        name = Name().generate_name()
        self.selected_name.delete(0, END)
        self.selected_name.insert(0, name['name'])
        self.selected_email.delete(0, END)
        self.selected_email.insert(0, name['email'])
        self.selected_address.delete(0, END)
        self.selected_address.insert(0, name['address'])
