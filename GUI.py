import tkinter as tk
from tkinter import *
from tkinter import ttk
import data.WebJsonIn
from selenium.webdriver.common.devtools.v127.storage import clear_shared_storage_entries

from config import *
import threading
import time

from data.WebJsonIn import WebJsonIn_data
from name import Name
from new_page import NewPage
from password_new import PasswordGenerator


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("工具合集")
        # self.geometry("400x300")

        # 创建一个容器，用于存放不同的页面
        self.container = ttk.Notebook(self)
        self.container.pack(expand=True, fill='both')

        # 创建页面
        self.page4 = Page4(self.container)
        self.page1 = Page1(self.container)
        self.page2 = Page2(self.container)
        self.page3 = Page3(self.container)
        self.page6 = Page6(self.container)
        self.page5 = Page5(self.container)

        # 添加页面到容器
        self.container.add(self.page4, text="浏览器操作工具")
        self.container.add(self.page1, text="页面生成器")
        self.container.add(self.page2, text="密码生成器")
        self.container.add(self.page3, text="虚拟信息生成器")
        self.container.add(self.page6, text="DNS导入模板")
        self.container.add(self.page5, text="其他")


class Page1(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
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
        new_page = NewPage(page_content)
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
        self.option1.pack()
        self.option2_var = tk.BooleanVar()
        self.option2 = tk.Checkbutton(self, text="使用字母", variable=self.option2_var)
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

class Page6(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text="DNS导入模板：")
        self.label.pack()

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



if __name__ == "__main__":
    app = App()
    app.mainloop()
