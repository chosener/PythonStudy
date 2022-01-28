# 2、可视化，取电影和评分

import csv

import matplotlib
from matplotlib import pyplot

# 通用字体设置
from matplotlib import font_manager

# my_font = font_manager.FontProperties(fname="字体的本地完整路径")
my_font = font_manager.FontProperties(fname="/Library/Fonts/Songti.ttc")

# pyplot.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# pyplot.style.use('seaborn')


f = open("data.csv", "r", encoding="utf-8")
csvReader = csv.reader(f)
name, score, year = [], [], []
for row in csvReader:
    name.append(row[0])
    year.append(row[1])
    score.append(row[2])

    try:
        # 获得下一个值:
        header_row = next(csvReader)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
pyplot.plot(name, score)
pyplot.title("电影排行榜")
pyplot.xlabel("电影")
pyplot.ylabel("评分")
pyplot.xticks(rotation=90)  # 控制横坐标的方向
pyplot.show()
