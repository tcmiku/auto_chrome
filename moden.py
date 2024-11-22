
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
from josn_pages.json_in import *
from tqdm import tqdm

from new_page import NewPage

class Moden:
    def __init__(self, driver,modes,domain_name):
        self.driver = driver
        if self.driver:
            self.driver.get("https://admin.shopify.com/")
            time.sleep(3)
            self.url = self.driver.current_url
            if modes is not None:
                page = NewPage(country=modes)
                if domain_name is not None:
                    self.new_page = page.add_page(domain_name)
                else:
                    print("输入域名不能为空")
            else:
                print("输入模式不能为空")
        else:
            print("传入driver错误")

    def switch_mode(self,mode):
        json_reader = JSON_IN('josn_pages/menu.json')
        menu_name = json_reader.read_json()
        self.menu_name = menu_name
        if mode == "swansumo":
            self.swansumo(menu_name[mode])
        elif mode == "grunsguru":
            self.grunsguru(menu_name[mode])
        elif mode == "grunsify":
            self.grunsify(menu_name[mode])
        else:
            print("输入模式错误")

    def swansumo(self,menu_name):
        pass

    def grunsguru(self,menu_name):
        new_names = menu_name.keys()
        try:
            self.process_pages_delete() #删除页面
        except Exception as e:
            print("页面删除功能ships_delete失败")
        try:
            self.process_pagesnew() #写入页面
        except Exception as e:
            print("页面写入功能ships_new失败")
        try:
            self.process_menus_new(new_names) #写入菜单
        except Exception as e:
            print("菜单写入功能menus_new失败")

    def grunsify(self,menu_name):
        pass

    def open_pages_new(self):
        self.driver.get(self.url + "/pages/new")
        print("开启页面pages_new")
        time.sleep(2)
        print("pages_new操作完成")

    def open_pages(self):
        self.driver.get(self.url + "/pages")
        print("开启页面pages")
        time.sleep(2)
        print("pages操作完成")

    def open_menus_new(self):
        self.driver.get(self.url + "/menus/new")
        print("开启页面menus_new")
        time.sleep(2)
        print("menus_new操作完成")

    def process_menus_new(self,new_names):
        driver = self.driver

        for name in new_names:
            self.open_menus_new()
            in_iframe = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  '//*[@id="AppFrameScrollable"]/div/div/div/div/div/div/iframe'))
            )
            driver.switch_to.frame(in_iframe)
            title_input = WebDriverWait(driver, 60).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME,
                                                  'Polaris-TextField__Input'))
            )
            title_input[0].send_keys(name)
            for i in self.menu_name[name]:
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
            # server_menu = WebDriverWait(driver, 60).until(
            #     EC.visibility_of_element_located((By.CSS_SELECTOR,
            #                                       '.Polaris-Button.Polaris-Button--pressable.Polaris-Button--variantPrimary.Polaris-Button--sizeMedium.Polaris-Button--textAlignCenter'))
            # )
            # server_menu.click()


    def process_pagesnew(self):
        driver = self.driver
        self.open_pages_new()
        url = driver.current_url
        url = url.replace('/pages/new', '')
        print("开始操作pages")

        pages_date = self.new_page

        for i in tqdm(range(1,len(pages_date)+1),desc="开始写入页面内容（内容较多写入会变慢）"):
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
            html_content = self.__split_string(pages_date[str('page'+str(i))]['content'], 400)
            for segments in tqdm(html_content,desc="正在写入分割后的页面内容"):
                html.send_keys(segments)
            time.sleep(1)
            page_server = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  '//*[@id="app"]/div[1]/div[1]/div/div[2]/form/div/div[3]/div/div/button[2]'))
            )
            if page_server.get_attribute('aria-disabled') != 'true':
                page_server.click()
                time.sleep(5)
            else:
                print("第"+str(i)+"页页面操作失败")
            if i != len(pages_date):
                driver.get(url + "/pages/new")
                time.sleep(5)
        print("pages页面操作完成")

    def __split_string(self,s, length):
        #字符串切割操作
        return [s[i:i + length] for i in range(0, len(s), length)]


    def process_pages_delete(self):
        driver = self.driver
        self.open_pages()
        try:
            print("开始操作pages_delete")
            in_iframe = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  "#AppFrameScrollable > div > div > div > div > div > div > iframe"))
            )
            driver.switch_to.frame(in_iframe)
            time.sleep(1)
            print("进入iframe")
            switch_bulltn = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/div[2]/div'))
            )
            switch_bulltn.click()
            time.sleep(2)
            actions_bulltn = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/button'))
            )
            actions_bulltn.click()
            time.sleep(0.5)
            Delete_pages = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  '.Polaris-ActionList__Item.Polaris-ActionList--destructive.Polaris-ActionList--default'))
            )
            Delete_pages.click()
            time.sleep(1)
            driver.switch_to.default_content()
            in_iframe = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                  "#dialogContainer > div > div > iframe"))
            )
            driver.switch_to.frame(in_iframe)
            time.sleep(1)
            delete_page_red = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  '//*[@id="app"]/div/div/div[3]/div/div/div[2]/button[2]'))
            )
            delete_page_red.click()
            print("页面删除成功")
            time.sleep(5)
        except Exception as e:
            print("页面删除失败可能无需删除")


def open_chrome(url,id):
    oepn_url = url + f"/api/v1/browser/start?user_id={id}&open_tabs=1"
    reget = requests.get(oepn_url)
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
            print("Error: ", web_date['msg'])
            return False


if __name__ == '__main__':
    url = "http://local.adspower.com:50325"
    chrome_id = "kmrsun0"
    domain_name = 'durri'
    mode = "grunsguru"
    driver = open_chrome(url,chrome_id)
    page =Moden(driver,mode,domain_name)
    page.switch_mode(mode)
