from main import *
class run_auto:
    def __init__(self,url,chrome_id,domain_name):
        # 打开浏览器
        autoweb_window = web(url)
        reget = autoweb_window.open_website(chrome_id)
        autoweb_link = autoweb_chrome()
        drivers = autoweb_link.linkwebsite(reget)

        #登录操作
        log_in = shopify_login()
        if log_in.login(drivers):
            print("开始自动化操作")
            print("程序暂停后有一分钟时间操作具体内容")
            auto_gui(drivers,domain_name)
            close_on = input("自动化操作完成是否关闭浏览器（0：否，1：是）：")

        # 关闭浏览器
        if close_on == "1":
            drivers.quit()
            autoweb_window.close_website(chrome_id)
            print("浏览器关闭成功(Webdriver closed successfully)")


    def auto_gui(drivers,domain_name):
        #导入需要用到的类和数据包
        sadelivery_josn = JSON_IN('josn_pages/shippinganddelivery.json')
        date = sadelivery_josn.read_json()
        open_auto = shopify_auto_page(drivers)
        control_auto = shopify_process(drivers)
        top_domain_name = domain_name.capitalize()
        #shippinganddelivery页面操作示例
        # open_auto.open_shippinganddelivery()
        # control_auto.new_process_shippinganddelivery(date)

        #markets页面操作示例
        # open_auto.open_markets()

        #appsandsaleschannels页面操作示例
        # open_auto.open_appsandsaleschannels()

        # general页面操作示例
        open_auto.open_general()
        control_auto.process_general(top_domain_name)

        #pages页面操作示例
        open_auto.open_pages_new()
        control_auto.process_pagesnew(domain_name)

if __name__ == '__main__':
    url = "http://local.adspower.com:50325"
    chrome_id = "kokywg6"
    domain_name = 'youdaak'
    run_auto(url,chrome_id,domain_name)