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

def process_pagesnew(dirver):
    dirver = dirver
    open_pages_new()
    url = driver.current_url
    url = url.replace('/pages/new', '')
    print("开始操作pages")

    pages_date = new_page

    for i in tqdm(range(1, len(pages_date) + 1), desc="开始写入页面内容（内容较多写入会变慢）"):
        iframe_element = driver.find_element(By.CSS_SELECTOR,
                                             "#AppFrameScrollable > div > div > div > div > div > div > iframe")
        driver.switch_to.frame(iframe_element)
        title = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.ID,
                                              "page-title"))
        )
        title.send_keys(pages_date[str('page' + str(i))]['title'])
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
        html_content = split_string(pages_date[str('page' + str(i))]['content'], 400)
        for segments in tqdm(html_content, desc="正在写入分割后的页面内容"):
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
            print("第" + str(i) + "页页面操作失败")
        if i != len(pages_date):
            driver.get(url + "/pages/new")
            time.sleep(5)
    print("pages页面操作完成")


def split_string(s,length):
    # 字符串切割操作
    return [s[i:i + length] for i in range(0, len(s), length)]


if __name__ == '__main__':
    pass