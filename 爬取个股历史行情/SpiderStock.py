
import requests
from bs4 import BeautifulSoup
from lxml import etree

#002352 顺丰控股

#2021年第四季度
#http://quotes.money.163.com/trade/lsjysj_002352.html?year=2021&season=4

stock_url = "http://quotes.money.163.com/trade/lsjysj_002352.html?year=2021&season=4"

req = requests.get(url=stock_url)

soup = BeautifulSoup(req.text,"lxml")
data = soup.find_all('tr')

data_list = soup.select('.table_bg001 border_box limit_sale > tbody > tr > td')

for item in data_list:
    print(item)

# tree = etree.HTML(req.text)
# data_list = tree.xpath('/html/body/div[2]/div[4]/table')
# print(data_list)