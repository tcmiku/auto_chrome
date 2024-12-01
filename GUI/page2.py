from tkinter import ttk
import tkinter as tk
from tkinter import *

from password_new import PasswordGenerator


class Page2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.line = Label(self, text="------------------------")
        self.line.pack()
        self.label_password = Label(self, text="密码生成器：")
        self.label_password.pack()

        self.label_length = Label(self, text="密码长度:")
        self.label_length.pack()

        self.length = Entry(self,width=5)
        self.length.insert(0, "10")
        self.length.pack()

        self.line = Label(self, text="------------------------")
        self.line.pack()

        self.option1_var = tk.BooleanVar()
        self.option1 = tk.Checkbutton(self, text="使用数字", variable=self.option1_var)
        self.option1.invoke()
        self.option1.pack()
        self.option2_var = tk.BooleanVar()
        self.option2 = tk.Checkbutton(self, text="使用字母", variable=self.option2_var)
        self.option2.invoke()
        self.option2.pack()
        self.option3_var = tk.BooleanVar()
        self.option3 = tk.Checkbutton(self, text="使用字符", variable=self.option3_var)
        self.option3.pack()

        self.line = Label(self, text="------------------------")
        self.line.pack()

        self.button_password = Button(self, text="生成密码", command=self.generate_password)
        self.button_password.pack()

        self.line = Label(self, text="------------------------")
        self.line.pack()

        self.password = Text(self, height=1, width=50)
        self.password.pack()

    def generate_password(self):
        length = int(self.length.get())
        user_digits = self.option1_var.get()
        use_letters = self.option2_var.get()
        use_special = self.option3_var.get()
        try:
            password = PasswordGenerator(length=length, use_digits=user_digits, use_letters=use_letters, use_special=use_special)
            password_result = password.generate_password()
            self.password.delete(1.0, END)
            self.password.insert(INSERT,password_result)
        except ValueError as e:
            print(e)

