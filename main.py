
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.ie.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tqdm import tqdm

import new_page
from josn_pages.json_in import *

from new_page import *

class web:
    def __init__(self,api_website):
        self.api_website = api_website

    def open_website(self,id):
        oepn_url = self.api_website + f"/api/v1/browser/start?user_id={id}&open_tabs=1"
        return requests.get(oepn_url)

    def close_website(self,id):
        oepn_url = self.api_website + f"/api/v1/browser/stop?user_id={id}"
        return requests.get(oepn_url)

class autoweb_chrome:
    def __init__(self):
        pass

    def linkwebsite(self,reget):
        if reget.status_code == 200:
            print("浏览器链接成功(Webdriver started successfully)")
            web_date = reget.json()
            if web_date['code'] == 0:
                print("获取webdrive成功(Get webdriver successfully)")
                chrome_path = web_date['data']['webdriver']
                service = Service(executable_path=chrome_path)
                chrome_options = Options()
                chrome_options.add_experimental_option("debuggerAddress", web_date["data"]["ws"]["selenium"])
                driver = webdriver.Chrome(service=service, options=chrome_options)
                return driver
            else:
                print("Error: ",web_date['msg'])
                return False

class shopify_login:
    def __init__(self):
        self.url = "https://www.shopify.com/login?ui_locales=en"

    def jianche(self,url):
        prefix = 'https://accounts.shopify.com/'
        no_login = 'https://admin.shopify.com/'
        print("检测是否需要登录")
        if url.startswith(prefix):
            return True
        elif url.startswith(no_login):
            return False
        else:
            return "NULL"

    def login(self,driver):
        driver.get(self.url)
        time.sleep(3)
        flag = self.jianche(url=driver.current_url)
        if flag:
            try:
                print("出现人机验证需要人为进入(请尽快完成人机验证只有60秒时间)")
                print("寻找登录按钮")
                # time.sleep(10)
                search_button = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                      ".ui-button.ui-button--primary.ui-button--full-width.ui-button--size-large.login-button.ui-button--has-hover-icon.captcha__submit"))
                )
                time.sleep(5)
                search_button.click()
                print("点击")
                time.sleep(1)
                search_button_login = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                      ".ui-button.ui-button--primary.ui-button--full-width.ui-button--size-large.ui-button--has-hover-icon.captcha__submit"))
                )
                time.sleep(5)
                search_button_login.click()
                print("登录成功")
                return True
            except  Exception as e:
                print("登录失败")
                return False
        elif flag != "NULL":
            print("无需登录")
            return True
        else:
            print("未知错误")

class shopify_auto_page:

    def __init__(self,drivers):
        time.sleep(1)
        self.driver = drivers
        self.url = str(drivers.current_url).split('?')[0]

    def open_shippinganddelivery(self):
        self.driver.get(self.url + "/settings/shipping")
        driver = self.driver
        print("开启页面shippinganddelivery")
        time.sleep(5)
        search_button_login = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "._SettingsItem__clickableAction_1mxsi_135"))
        )
        time.sleep(1)
        search_button_login.click()
        time.sleep(2)
        print("shippinganddelivery操作完成")

    def open_markets(self):
        self.driver.get(self.url + "/settings/markets")
        driver = self.driver
        print("开启页面markets")
        time.sleep(5)
        print('markets操作完成')

    def open_appsandsaleschannels(self):
        self.driver.get(self.url + "/settings/apps")
        driver = self.driver
        print("开启页面appsandsaleschannels")
        time.sleep(5)
        print("appsandsaleschannels操作完成")

    def open_general(self):
        self.driver.get(self.url + "/settings/general")
        print("开启页面general")
        time.sleep(5)
        print("general操作完成")

    def open_pages_new(self):
        self.driver.get(self.url + "/pages/new")
        print("开启页面pages_new")
        time.sleep(5)
        print("pages_new操作完成")

    def open_pages(self):
        self.driver.get(self.url + "/pages")
        print("开启页面pages")
        time.sleep(5)
        print("pages操作完成")

    def open_navigation(self):
        self.driver.get(self.url + "/menus")
        print("开启页面navigation")
        time.sleep(5)
        print("navigation操作完成")

class shopify_process:
    """
    自动化操作各个页面
    new开头的方法为新店铺配置
    """
    def __init__(self,driver):
        self.driver = driver

    def process_general(self,storename:str,storephone='36954338'):
        """
        自动化操作店铺设置中的店铺名和电话号码
        storename: 店铺名
        """
        driver = self.driver
        print("开始操作general")
        dev_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "._SettingsItem__wrapper_1mxsi_145"))
        )
        # 创建 ActionChains 对象
        actions = ActionChains(driver)
        print("将鼠标移动到 dev 元素上")
        actions.move_to_element(dev_element).perform()

        time.sleep(1)
        search_button = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".Polaris-Button.Polaris-Button--pressable.Polaris-Button--variantTertiary.Polaris-Button--sizeMedium.Polaris-Button--textAlignCenter.Polaris-Button--iconOnly"))
        )
        time.sleep(1)
        search_button.click()
        input_fields = driver.find_elements(By.CSS_SELECTOR, ".Polaris-TextField__Input")
        in_storename = input_fields[0]
        time.sleep(0.5)
        in_storename.send_keys(Keys.CONTROL + "a")
        time.sleep(0.5)
        in_storename.send_keys(storename)
        in_phone = input_fields[1]
        in_phone.send_keys(Keys.CONTROL + "a")
        time.sleep(0.5)
        in_phone.send_keys(storephone)
        time.sleep(0.5)
        print("修改店铺名和电话号码完成")
        search_button_server = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".Polaris-Button.Polaris-Button--pressable.Polaris-Button--variantPrimary.Polaris-Button--sizeMedium.Polaris-Button--textAlignCenter"))
        )
        if search_button_server.get_attribute('aria-disabled') != 'true':
            time.sleep(1)
            search_button_server.click()
            time.sleep(3)
            print("General页面操作完成")
        else:
            print("按钮不可点击")
            print("General页面操作完成")



    def  new_process_shippinganddelivery(self,date,country='us'):
        driver = self.driver
        print("开始操作shippinganddelivery")
        element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#settings-body > div > div:nth-child(2) > div > div:nth-child(1) > div > div.Polaris-BlockStack > div > div > div > div > div > div:nth-child(3) > div > div > div > div > div:nth-child(2) > div > div > div > span > span"))
        )
        # 获取该元素的文字内容
        text_content = element.text
        #如果有HK的条目，则删除
        if text_content == "Domestic • Hong Kong SAR":
            del_bullton = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  "#settings-body > div > div:nth-child(2) > div > div:nth-child(1) > div > div.Polaris-BlockStack > div > div > div > div > div > div:nth-child(3) > div > div > div > div > div.Polaris-BlockStack > div > div > button"))
            )
            del_bullton.click()
            time.sleep(0.5)
            del_red_button = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  ".Polaris-ActionList__Item.Polaris-ActionList--destructive.Polaris-ActionList--default"))
            )
            del_red_button.click()
            time.sleep(3)
            search_button_server = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  ".Polaris-Button.Polaris-Button--pressable.Polaris-Button--variantPrimary.Polaris-Button--sizeMedium.Polaris-Button--textAlignCenter"))
            )
            search_button_server.click()
            time.sleep(3)
            print('HK条目删除成功')

        print("开始添加物流信息")
        print("物流信息1添加开始")
        self.__Addrate()
        time.sleep(1)
        self.__Addrate_add(name=date[country]['addrate1']['name'], min_price=date[country]['addrate1']['price_min'])
        print("物流信息1添加完成")
        search_button_server = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".Polaris-Button.Polaris-Button--pressable.Polaris-Button--variantPrimary.Polaris-Button--sizeMedium.Polaris-Button--textAlignCenter"))
        )
        search_button_server.click()
        time.sleep(5)
        print("物流信息2添加开始")
        self.__Addrate()
        time.sleep(1)
        self.__Addrate_add(name=date[country]['addrate2']['name'], min_price=date[country]['addrate2']['price_min'],
                           price=date[country]['addrate2']['price'], max_price=date[country]['addrate2']['price_max'],
                           num_int=2)
        print("物流信息2添加完成")
        time.sleep(1)
        # print('开始设置地区')
        # self.__Editzone_open()
        # self.__Editzone_add()
        search_button_server = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".Polaris-Button.Polaris-Button--pressable.Polaris-Button--variantPrimary.Polaris-Button--sizeMedium.Polaris-Button--textAlignCenter"))
        )
        search_button_server.click()
        time.sleep(5)
        print("shippinganddelivery页面操作完成")

    def __Addrate(self):
        driver = self.driver
        add_bullton = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "._SettingsItem_1mxsi_31._SettingsItem--clickable_1mxsi_68._Button_xz0d6_4._Button--withPlusIcon_xz0d6_1"))
        )
        add_bullton.click()
        time.sleep(1)

    def __Addrate_add(self,name:str,min_price:str,price=None,max_price=None,num_int=1):

        driver = self.driver
        add_rate = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".Polaris-TextField__Input"))
        )
        add_rate.send_keys(name)
        add_rate_price = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID,
                                              "Rates-Cost-TextField"))
        )
        add_rate_price.send_keys(Keys.CONTROL + "a")
        time.sleep(0.5)
        if price is not None:
            add_rate_price.send_keys(price)
        add_bullton = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".Polaris-Text--root.Polaris-Text--bodyMd.Polaris-Text--regular"))
        )
        time.sleep(0.5)
        if num_int == 1:
            add_bullton.click()
        time.sleep(0.5)
        switch_bullton = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#conditional-pricing-collapsible > div > div.Polaris-BlockStack > label:nth-child(2)"))
        )
        switch_bullton.click()
        time.sleep(0.5)
        min_bullton = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID,
                                              "minimum-condition-field"))
        )
        min_bullton.send_keys(min_price)
        max_bullton = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID,
                                              "maximum-condition-field"))
        )
        if max_price is not None:
            max_bullton.send_keys(max_price)
            time.sleep(0.5)

        server_bullton = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//button[@class='Polaris-Button Polaris-Button--pressable Polaris-Button--variantPrimary Polaris-Button--sizeMedium Polaris-Button--textAlignCenter']"))
        )
        server_bullton.click()
        time.sleep(3)

    def __Editzone_open(self):
        driver = self.driver
        print('点击Edit_zone')
        edit_bullton = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#settings-body > div > div:nth-child(2) > div > div:nth-child(1) > div > div.Polaris-BlockStack > div > div > div > div > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div.Polaris-BlockStack > div > div > button"))
        )
        edit_bullton.click()
        time.sleep(0.5)
        edit_bullton_1 = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".Polaris-ActionList__Item.Polaris-ActionList--default"))
        )
        edit_bullton_1.click()
        time.sleep(0.5)

    def __Editzone_add(self):
        driver = self.driver
        divs = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@class="_ListHeader__CollapsibleButton_1nbgz_52"]'))
        )
        # 遍历这些元素并进行点击操作
        for element in divs:
            element.click()
            time.sleep(0.5)  # 每次点击后等待0.5秒

    def process_pagesnew(self,web):
        driver = self.driver
        url = driver.current_url
        url = url.replace('/pages/new', '')
        print("开始操作pages")
        pages = new_page.NewPage()
        pages_date = pages.add_page(web)

        for i in tqdm(range(1,len(pages_date)+1)):
            iframe_element = driver.find_element(By.CSS_SELECTOR,
                                                 "#AppFrameScrollable > div > div > div > div > div > div > iframe")
            driver.switch_to.frame(iframe_element)
            title = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID,
                                                  "page-title"))
            )
            title.send_keys(pages_date[str('page'+str(i))]['title'])
            html_mode = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  '//*[@class="QTKzU"]/span/button'))
            )
            html_mode.click()
            time.sleep(0.5)
            html = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID,
                                                  "page-description"))
            )
            print("开始写入页面内容（内容较多写入会变慢）")
            html.send_keys(pages_date[str('page'+str(i))]['content'])
            time.sleep(1)
            print("页面编辑完成")
            page_server = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  '//*[@id="app"]/div[1]/div[1]/div/div[2]/form/div/div[3]/div/div/button[2]'))
            )
            if page_server.get_attribute('aria-disabled') != 'true':
                page_server.click()
                time.sleep(5)
                print("第"+str(i)+"页页面操作完成")
            else:
                print("第"+str(i)+"页页面操作失败")
            if i != 7:
                driver.get(url + "/pages/new")
                time.sleep(5)
        print("pages页面操作完成")

    def process_pages_delete(self):
        driver = self.driver
        print("开始操作pages_delete")
        print("未完成")

    def process_navigation(self):
        driver = self.driver
        url = driver.current_url
        print("开始操作navigation")

        in_iframe = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#AppFrameScrollable > div > div > div > div > div > div > iframe"))
        )
        driver.switch_to.frame(in_iframe)
        time.sleep(1)
        open_Footer_menu = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="app"]/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/th/p/a'))
        )
        open_Footer_menu.click()
        print("Footer菜单打开")
        driver.switch_to.default_content()
        time.sleep(3)
        in_iframe = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '#AppFrameScrollable > div > div > div > div > div > div > iframe'))
        )
        driver.switch_to.frame(in_iframe)
        print("进入iframe")
        add_menu = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="node-ROOT-add-node"]/div/div/button'))
        )
        add_menu.click()
        time.sleep(1)
        add_menu_item = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '.Polaris-TextField__Input.Polaris-TextField__Input--hasClearButton'))
        )
        add_menu_item.click()
        time.sleep(1)
        menu_items = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME,
                                              'Online-Store-UI-UrlPickerList-UrlPickerItem__Text_192hg'))
        )
        menu_items[4].click()
        time.sleep(2)
        menu_items_list = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME,
                                              'Online-Store-UI-UrlPickerList-UrlPickerItem__Text_192hg'))
        )
        #菜单添加操作
        for i in tqdm(range(len(menu_items_list)),desc="navigation菜单添加"):
            menu_items_list[i].click()
            time.sleep(0.5)
            server_item = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  '//*[@id="app"]/div[1]/div[1]/div[1]/div/div/div/div[3]/div/button[2]'))
            )
            time.sleep(0.5)
            server_item.click()
            if i != 6:
                add_menu = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.XPATH,
                                                      '//*[@id="node-ROOT-add-node"]/div/div/button'))
                )
                add_menu.click()
                time.sleep(1)
                add_menu_item = WebDriverWait(driver, 60).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                      '.Polaris-TextField__Input.Polaris-TextField__Input--hasClearButton'))
                )
                add_menu_item.click()
                time.sleep(1)
                menu_items = WebDriverWait(driver, 60).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME,
                                                         'Online-Store-UI-UrlPickerList-UrlPickerItem__Text_192hg'))
                )
                menu_items[4].click()
                time.sleep(5)
                menu_items_list = WebDriverWait(driver, 60).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME,
                                                         'Online-Store-UI-UrlPickerList-UrlPickerItem__Text_192hg'))
                )

        driver.switch_to.default_content()
        time.sleep(2)
        in_iframe = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '#AppFrameScrollable > div > div > div > div > div > div > iframe'))
        )
        driver.switch_to.frame(in_iframe)
        print("footer_menu添加完成")
        server_menu = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '.Polaris-Text--root.Polaris-Text--bodySm.Polaris-Text--semibold'))
        )
        server_menu.click()
        time.sleep(1)
        print('Footer_menu导航完成')



        driver.get(url)
        in_iframe = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#AppFrameScrollable > div > div > div > div > div > div > iframe"))
        )
        driver.switch_to.frame(in_iframe)
        time.sleep(1)
        open_Footer_menu = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="app"]/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/table/tbody/tr[2]/th/p/a'))
        )
        open_Footer_menu.click()
        print("Main_menu菜单打开")
        driver.switch_to.default_content()
        time.sleep(3)
        in_iframe = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '#AppFrameScrollable > div > div > div > div > div > div > iframe'))
        )
        driver.switch_to.frame(in_iframe)
        print("进入iframe")
        add_menu = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="node-ROOT-add-node"]/div/div/button'))
        )
        add_menu.click()
        time.sleep(1)
        add_menu_item = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '.Polaris-TextField__Input.Polaris-TextField__Input--hasClearButton'))
        )
        add_menu_item.click()
        time.sleep(1)
        menu_items = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME,
                                              'Online-Store-UI-UrlPickerList-UrlPickerItem__Text_192hg'))
        )
        menu_items[4].click()
        time.sleep(2)
        menu_items_list = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME,
                                              'Online-Store-UI-UrlPickerList-UrlPickerItem__Text_192hg'))
        )
        menu_items_list[2].click()
        time.sleep(0.5)
        server_item = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="app"]/div[1]/div[1]/div[1]/div/div/div/div[3]/div/button[2]'))
        )
        time.sleep(0.5)
        server_item.click()
        add_menu = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="node-ROOT-add-node"]/div/div/button'))
        )
        add_menu.click()
        time.sleep(1)
        add_menu_item = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '.Polaris-TextField__Input.Polaris-TextField__Input--hasClearButton'))
        )
        add_menu_item.click()
        time.sleep(1)
        menu_items = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME,
                                                 'Online-Store-UI-UrlPickerList-UrlPickerItem__Text_192hg'))
        )
        menu_items[4].click()
        time.sleep(5)
        menu_items_list = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME,
                                                 'Online-Store-UI-UrlPickerList-UrlPickerItem__Text_192hg'))
        )
        menu_items_list[1].click()
        time.sleep(0.5)
        server_item = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="app"]/div[1]/div[1]/div[1]/div/div/div/div[3]/div/button[2]'))
        )
        time.sleep(0.5)
        server_item.click()
        time.sleep(1)

        driver.switch_to.default_content()
        time.sleep(2)
        in_iframe = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '#AppFrameScrollable > div > div > div > div > div > div > iframe'))
        )
        driver.switch_to.frame(in_iframe)
        print("Main_menu添加完成")
        server_menu = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '.Polaris-Text--root.Polaris-Text--bodySm.Polaris-Text--semibold'))
        )
        server_menu.click()
        print('Main_menu导航完成')
        time.sleep(1)
        print("navigation页面操作完成")