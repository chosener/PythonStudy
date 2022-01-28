
import requests
from bs4 import BeautifulSoup
from lxml import etree
import xlwt
import pandas as pd

#002352 顺丰控股

# 请求headers 模拟谷歌浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

#2021年第四季度
#http://quotes.money.163.com/trade/lsjysj_002352.html?year=2021&season=4

stock_url = "http://quotes.money.163.com/trade/lsjysj_002352.html?year=2021&season=4"

req = requests.get(url=stock_url,headers= headers)
req.encoding = req.apparent_encoding

# print(req.text)

soup = BeautifulSoup(req.text,"lxml")

table = soup.select('body > div.area > div.inner_box > table')

tf = pd.read_html(stock_url)

# print(tf[3])

tf[3].to_csv('data1.csv')

# soup_list = BeautifulSoup(table.text,"lxml")
# print(soup_list.text)

#标题
# title = soup.find_all('th')
# print('title:',title)
#
# data_list_title = []
# for data in title:
#     data_list_title.append(data.text.strip())
#
# # print(data_list_title)
#
# #内容处理
# content = soup.find_all('td')
# data_list_content = []
# for data in content:
#     data_list_content.append(data.text.strip())
#
# new_list = [data_list_content[i:i+11] for i in range(0,len(data_list_content),11)]
#
# # 存入excel表格
# book = xlwt.Workbook()
# sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)
#
# # 标题存入
# heads = data_list_title[:]  # 将data_list_title第一位到最后一位赋值给heads
# ii = 0
# for head in heads:
#     sheet1.write(0, ii, head)
#     ii += 1
#
# # 内容录入
# i = 1
# for list in new_list:
#     j = 0
#     # print('==================', list)
#     for data in list:
#         data = 'xxx' if data == '' else data
#         sheet1.write(i, j, data)
#         j += 1
#     i += 1
# # 文件保存
# book.save('./data.xls')

print('全部完成!!!')