from main import *
class run_auto:
    def __init__(self,url,chrome_id,domain_name,country = 'us'):
        self.url = url
        self.chrome_id = chrome_id
        self.domain_name = domain_name
        self.country = country

    def auto(self):
        # 打开浏览器
        autoweb_window = web(self.url)
        reget = autoweb_window.open_website(self.chrome_id)
        autoweb_link = autoweb_chrome()
        drivers = autoweb_link.linkwebsite(reget)

        #登录操作
        log_in = shopify_login()
        if log_in.login(drivers):
            print("开始自动化操作")
            print("程序暂停后有一分钟时间操作具体内容")
            self.auto_gui(drivers,self.domain_name,)

        # drivers.get('https://www.browserscan.net/')
        # close_on = input("自动化操作完成是否关闭浏览器（0：否，1：是）：")
        #
        # # 关闭浏览器
        # if close_on == "1":
        #     drivers.quit()
        #     autoweb_window.close_website(chrome_id)
        #     print("浏览器关闭成功(Webdriver closed successfully)")


    def auto_gui(self,drivers,domain_name):
        #导入需要用到的类和数据包
        sadelivery_josn = JSON_IN('josn_pages/shippinganddelivery.json')
        date = sadelivery_josn.read_json()
        open_auto = shopify_auto_page(drivers)
        control_auto = shopify_process(drivers)
        top_domain_name = domain_name.capitalize()

        # #markets页面操作示例
        # open_auto.open_markets()
        # control_auto.process_markets_new()
        open_auto.open_markets()
        control_auto.process_add_market()
        #shippinganddelivery页面操作示例
        open_auto.open_shippinganddelivery()
        control_auto.new_process_shippinganddelivery(date)


        #appsandsaleschannels页面操作示例
        open_auto.open_appsandsaleschannels()

        # general页面操作示例
        open_auto.open_general()
        control_auto.process_general(top_domain_name)
        #
        #pages_delete页面操作示例(用于删除页面)
        open_auto.open_pages()
        control_auto.process_pages_delete()
        #
        #pages_new页面操作示例
        open_auto.open_pages_new()
        control_auto.process_pagesnew(domain_name,self.country)
        #
        #navigation页面操作示例
        open_auto.open_navigation()
        control_auto.process_navigation()

if __name__ == '__main__':
    url = "http://local.adspower.com:50325"
    chrome_id = "kp6kfw9"
    domain_name = 'houblae'
    run_auto(url,chrome_id,domain_name).auto()