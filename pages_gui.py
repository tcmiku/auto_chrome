from new_page import *
from tkinter import *
from password_new import *

class PagesGUI:

    def __init__(self, master):
        self.index = 0
        self.master = master
        self.master.geometry("700x550")
        self.master.title("页面内容生成器")

        self.label = Label(self.master, text="页面内容生成器：")
        self.label.pack()

        self.label_name = Label(self.master, text="输入域名:")
        self.label_name.pack()

        # 输入框
        self.selected_name = Entry(self.master)
        self.selected_name.pack()

        # 下拉选择框
        self.label_content = Label(self.master, text="选择模板内容:")
        self.label_content.pack()
        self.page_contents = ["us","de","swansumo","grunsguru","grunsify"]  # 示例页面内容
        self.selected_content = StringVar(self.master)
        self.selected_content.set(self.page_contents[0])  # 设置默认值
        self.dropdown_content = OptionMenu(self.master, self.selected_content, *self.page_contents)
        self.dropdown_content.pack()

        #分界线
        self.line = Label(self.master, text="-----------------------------------------")
        self.line.pack()
        # 创建按钮
        self.button_create = Button(self.master, text="生成", command=self.create_page)
        self.button_create.pack()

        self.line = Label(self.master, text="-----------------------------------------")
        self.line.pack()

        self.label_title = Label(self.master, text="网页标题:")
        self.label_title.pack()
        self.text_title = Text(self.master, height=1, width=50)
        self.text_title.pack()

        self.button_next = Button(self.master, text="下一页", command=self.next_page,width=15)
        self.button_next.pack(side=RIGHT)
        self.button_back = Button(self.master, text="上一页", command=self.back_page,width=15)
        self.button_back.pack(side=LEFT)

        self.label_content = Label(self.master, text="网页内容:")
        self.label_content.pack()
        self.text_content = Text(self.master, height=10, width=60)
        self.text_content.pack()

        self.button_copy = Button(self.master, text="复制", command=self.copy_content)
        self.button_copy.pack()

        self.line = Label(self.master, text="------------------------")
        self.line.pack()
        self.label_password = Label(self.master, text="密码生成器：")
        self.label_password.pack()
        self.password = Text(self.master, height=1, width=50)
        self.password.pack()
        self.button_password = Button(self.master, text="生成密码", command=self.generate_password)
        self.button_password.pack()



    def create_page(self):
        self.index = 0
        self.title_list = []
        self.content_list = []
        page_name = self.selected_name.get()
        page_content = self.selected_content.get()
        new_page = NewPage(page_content)
        page_data =new_page.add_page(page_name)
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

    def generate_password(self):
        password = PasswordGenerator(length=10, use_digits=True, use_letters=True, use_special=False)
        password_result = password.generate_password()
        self.password.delete(1.0, END)
        self.password.insert(INSERT,password_result)

if __name__ == "__main__":
    root = Tk()
    app = PagesGUI(root)
    root.mainloop()
