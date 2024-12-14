from statistics import pstdev

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from josn_pages.json_in import JSON_IN
import Driver
import time


def navigation(url:str,chrome_id:str,oldnavig:bool,file_path:str,country:str):
    menu_data =json_data(file_path)
    menu_data = menu_data[count]
    driver = Driver.open_chrome(url, chrome_id)
    driver.get("https://admin.shopify.com/")
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CLASS_NAME,
                                          'Polaris-Avatar__Svg'))
    )   #等待页面加载完成
    url = driver.current_url
    open_navigation_menu(driver,url)

    new_menuslit = list()
    del_menuslsit = list()

    if oldnavig:    #新老导航判断 true为老导航 false为新导航
        menus_iframe(driver,classname='_Frame_1lmrp_1')

        Menuslist =WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.XPATH,
                                              '//p[@class="b0VHw"]/a'))
        )   #等待菜单加载完成

        for i in Menuslist: #获取nav菜单中的链接
            print(i.get_attribute('href'))
            new_text = i.text.replace(" ","")
            print(new_text)
            if new_text in ["Footermenu","Mainmenu"]:
                new_menuslit.append(i.get_attribute('href'))
            else:
                del_menuslsit.append(i.get_attribute('href'))

        for i in del_menuslsit:  #删除nav菜单中的链接
            driver.get(i)
            del_menus(driver)

        for i in new_menuslit:  #导航添加
            driver.get(i)
            add_menus(driver)
    else:
        Menuslist = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                 '.Polaris-Link.Polaris-Link--monochrome.Polaris-Link--removeUnderline'))
        )  # 等待菜单加载完成
        for i in Menuslist:
            link = i.get_attribute('href')
            new_text = i.text.replace(" ", "")
            if new_text in ["Footermenu", "Mainmenu","Customeraccountmainmenu"]:
                new_menuslit.append(link)
            else:
                del_menuslsit.append(link)

        print(del_menuslsit)
        for i in del_menuslsit:  # 删除nav菜单中的链接
            driver.get(i)
            del_new_menus(driver)
            time.sleep(1)

        for i in new_menuslit:  # 导航添加
            driver.get(i)
            del_add_new_menus(driver,menu_data)
            add_new_menus(driver,menu_data)

def add_new_menus(driver,menu_data):
    Name = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        '.Polaris-TextField__Input'))
    )
    print(Name.text)
    add_menus_btn = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                             '._Content_tsr3k_153._focusRing_tsr3k_141'))
    )
    new_name = Name.get_attribute("value").replace(" ", "_")
    menu = list(menu_data[new_name].keys())
    menu_list = []
    menu2 = []
    meun1 = set(menu)
    for i in add_menus_btn:
        new_text = i.text
        menu2.append(new_text)
    menu2 = set(menu2)
    menu_list = list(meun1 - menu2)
    print(menu_list)
    if len(menu_list) > 0:
        for i in menu_list:
            pass

def add_menu_item(driver):
    add = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.NAME,
                                        '_AddNode_1z03p_13 _RootAddNode_1hek5_6'))
    )
    add.click()


def del_add_new_menus(driver,menu_data):
    Name = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                          '.Polaris-TextField__Input'))
    )
    print(Name.text)
    add_menus_btn = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                          '._Content_tsr3k_153._focusRing_tsr3k_141'))
    )
    li_id = li(driver)
    index = 0
    for i in add_menus_btn:
        print(i.text)
        new_name = Name.get_attribute("value").replace(" ","_")
        new_text = i.text
        if new_name == "Main_menu":
            if new_text in menu_data[new_name].keys():
                print("不用删除")
                index += 1
            else:
                print("删除")
                i.click()
                ioch_button(driver,li_id[index])
                index += 1
        else:
            if new_text in menu_data[new_name].keys():
                print("不用删除")
                index += 1
            else:
                print("删除")
                i.click()
                ioch_button(driver,li_id[index])
                index += 1

def ioch_button(driver,id):
    ioch_id = "delete-node-button-"+id
    del_menus_btn = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID,
                                          ioch_id))
    )
    del_menus_btn.click()
    del_btn = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          ".Polaris-Button.Polaris-Button--pressable.Polaris-Button--variantPrimary.Polaris-Button--sizeMedium.Polaris-Button--textAlignCenter.Polaris-Button--toneCritical"))
    )
    del_btn.click()
    del_server_btn = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          ".Polaris-Button.Polaris-Button--pressable.Polaris-Button--variantPrimary.Polaris-Button--sizeMedium.Polaris-Button--textAlignCenter"))
    )
    del_server_btn.click()

def li(driver):
    li_list = []
    del_menus_btn = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.XPATH,
                                          '//*[@class="_Subtree_1i7yb_1"]//li'))
    )
    for i in del_menus_btn:
        id = i.get_attribute("id")
        li_list.append(id.split("-")[1])
    return li_list

def del_new_menus(driver):
    del_menus_btn = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID,
                                          'delete-menu-button'))
    )  # 删除菜单按钮
    del_menus_btn.click()
    Delete_menus_btn = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                          '.Polaris-Text--root.Polaris-Text--bodySm.Polaris-Text--semibold'))
    )  # 删除按钮
    for i in Delete_menus_btn:
        new_text = i.text.replace(" ", "")
        if new_text == "Deletemenu":
            i.click()
            break


def open_navigation_menu(driver,url):
    driver.get(url+"/menus")

def menus_iframe(driver,classname):
    menus_iframe =WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CLASS_NAME,
                                          classname))
        )   #进入iframe
    driver.switch_to.frame(menus_iframe)

def add_menus(driver):          #添加菜单
    driver.switch_to.default_content()
    menus_iframe(driver,classname='_Frame_1lmrp_1')
    del_menus_btn =WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                          '.Polaris-Text--root.Polaris-Text--bodySm.Polaris-Text--medium'))
        )
    for i in del_menus_btn:
        items_delete(driver,i)

def add_menu_item(driver):
    pass

def items_delete(driver,del_menus_btn):
    if del_menus_btn.text == "Delete":
        del_menus_btn.click()
    driver.switch_to.default_content()
    menus_iframe(driver,classname='_Iframe_pivoa_21')
    del_menus_confirm_btn =WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH,
                                          '/html/body/div/div/div/div[3]/div/div/div[2]/button[2]'))
        )
    del_menus_confirm_btn.click()


def del_menus(driver):
    driver.switch_to.default_content()
    menus_iframe(driver,classname='_Frame_1lmrp_1')
    del_menus_btn =WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID,
                                          'delete-menu-button'))
        )   #删除菜单按钮
    del_menus_btn.click()
    driver.switch_to.default_content()
    menus_iframe(driver,classname='_Iframe_pivoa_21')
    # _Iframe_pivoa_21
    del_menus_confirm_btn =WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH,
                                          '/html/body/div/div/div/div[3]/div/div/div[2]/button[2]'))
        )   #确认删除按钮
    del_menus_confirm_btn.click()

def json_data(file_path):
    data = JSON_IN(file_path)
    return data.read_json()

if __name__ == '__main__':
    url = "http://local.adspower.com:50325"
    chrome_id = "kr4kvwm"
    file = "E:\py\web\pythonProject1\josn_pages\menus.json"
    count = "us"
    navigation(url,chrome_id,oldnavig=False,file_path=file,country=count)
    # driver.switch_to.default_content()
    # json_data()