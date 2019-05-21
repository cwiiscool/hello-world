from selenium.webdriver import Chrome
from app01.spider import monogo
import pymysql
import time

drive = Chrome(r'D:\pyth\爬虫\爬取汽车的数据\chromedriver.exe')
conn = pymysql.connect()
for id in range(1,6):
    url = 'https://mall.autohome.com.cn/list/0-310100-0-0-7-0-0-0-0-'+ str(id) +'.html?minPrice=50'
    print(url)
    drive.get(url)
    drive.implicitly_wait(10)
    lists = drive.find_element_by_class_name("list")
    classs = lists.find_element_by_class_name('fn-clear')
    lis = classs.find_elements_by_class_name('carbox')
    print('第%s次请求网络' %id)
    for li in lis:
        aas = li.find_elements_by_css_selector(' a div')[3]
        ccs = li.find_elements_by_css_selector(' a div')[4]
        bbs = li.find_elements_by_css_selector(' a div')[1]
        link = bbs.find_element_by_css_selector('img').get_attribute('src')
        title = aas.get_attribute('title')
        brief  =ccs.get_attribute('title')
        dic = {"link":link, "title": title, 'brief':brief,"id": id}
        monogo.insert_data(dic)

