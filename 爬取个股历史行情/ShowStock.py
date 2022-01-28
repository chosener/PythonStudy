# 2、可视化，取电影和评分

import csv
from matplotlib import pyplot

pyplot.rcParams['font.sans-serif'] = ['Arial']  # 用来正常显示中文标签
f = open("data1.csv", "r", encoding="utf-8")
csvReader = csv.reader(f)
price, year = [], []
for row in csvReader:
    year.append(row[0])
    price.append(row[4])
    header_row = next(csvReader)
pyplot.plot(year, price)
pyplot.title("收盘价")
pyplot.xlabel("日期")
pyplot.ylabel("价格")
pyplot.xticks(rotation=90)  # 控制横坐标的方向
pyplot.show()