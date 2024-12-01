import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.service import Service


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
    else:
        print("Error: ", reget.status_code)
        return False

if __name__ == '__main__':
    url = "http://local.adspower.com:50325"
    chrome_id = "ko0j78v"
    driver = open_chrome(url, chrome_id)