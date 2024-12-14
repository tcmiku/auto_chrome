import tkinter as tk
from tkinter import ttk


from page1 import Page1
from page2 import Page2
from page3 import Page3
from page4 import Page4
from page5 import Page5
from page6 import Page6


class App(tk.Tk):
    flage = False
    def __init__(self):
        super().__init__()
        self.title("工具合集")
        # self.geometry("400x300")
        # 创建自定义标题栏
        title_bar = tk.Frame(self, bg='lightgray', relief='raised', bd=2)
        title_bar.pack(fill=tk.X)

        # 创建自定义按钮
        custom_button = tk.Button(title_bar, text="置顶窗口", command=self.top)
        custom_button.pack(side=tk.LEFT, padx=5, pady=2)


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

    def top(self):
        self.flage = not self.flage
        self.attributes("-topmost", self.flage)



if __name__ == "__main__":
    app = App()
    app.mainloop()
