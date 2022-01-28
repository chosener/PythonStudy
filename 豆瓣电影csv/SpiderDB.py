# 1、爬取内容，写进csv文件
import requests
import re
import csv

# 豆瓣电影排行榜，写进csv文件
url = "https://movie.douban.com/top250?start=25"  # start确定每次起始位置，每次取25个

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}
res = requests.get(url, headers=headers)
page_content = res.text
# .*?表示懒惰匹配，加上括号表示要取匹配的内容，?P<name>表示根据此标记获取匹配的内容，使用下面group时候用
# 正则预编译
obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp;'
                 r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<coment>.*?)人评价</span>', re.S)

result = obj.finditer(page_content)  # 生成的内容是个迭代器
f = open("data.csv", "a+", encoding="utf-8")
csvwriter = csv.writer(f)

for it in result:
    # print(it.group('name')) #对应?P<name>，可以用过name标记取到匹配的内容
    # print(it.group('year').strip())#处理年份前面的空格
    # print(it.group('score'))
    # print(it.group('coment'))
    dic = it.groupdict()  # 把数据装进字典
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
print("over")