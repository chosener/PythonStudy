# 2、可视化，取电影和评分

import csv

import matplotlib
from matplotlib import pyplot, font_manager

# 通用字体设置
from matplotlib import font_manager as fm, rcParams
from matplotlib.font_manager import FontManager

mpl_fonts = set(f.name for f in FontManager().ttflist)

# print('all font list get from matplotlib.font_manager:')
# for f in sorted(mpl_fonts):
#     print('\t' + f)

#Fira Code
# matplotlib.rc("font", family='Arial')

# 定义自定义字体，文件名从查看系统中文字体中来

# myfont = font_manager.FontProperties(fname='/Users/samdong/opt/anaconda3/envs/python39/lib/python3.9/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf')
# # 解决负号'-'显示为方块的问题
# matplotlib.rcParams['axes.unicode_minus'] = False

# my_font = font_manager.FontProperties(fname="字体的本地完整路径")
# my_font = font_manager.FontProperties(fname="/Library/Fonts/Songti.ttc")

# pyplot.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# pyplot.rcParams['axes.unicode_minus'] = False #用来正常显示负号
# pyplot.style.use('seaborn')

# font = {'family' : 'SimHei',
#         'weight' : 'bold',
#         'size'   : '16'}
# pyplot.rc('font', **font)  # pass in the font dict as kwargs
# pyplot.rc('axes',unicode_minus=False)


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
