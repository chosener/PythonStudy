
#爬取西游记

#https://www.shicimingju.com/book/xiyouji.html

import requests
from bs4 import BeautifulSoup



def SpiderXiYou():
    headers = {
        'user - agent': 'Mozilla / 5.0(Macintosh; Intel  Mac  OS   X    10_15_7) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 97.0 .4692 .99     Safari / 537.36'
    }
    url = "https://www.shicimingju.com/book/xiyouji.html"
    page_resp = requests.get(url=url,headers=headers)
    page_resp.encoding = 'utf-8'
    page_text = page_resp.text
    # print(page_text)
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('#main_left > div > div.book-mulu > ul > li')
    fp = open('./xiyou.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        detail_page_resp = requests.get(detail_url,headers=headers)
        detail_page_resp.encoding = 'utf-8'
        detail_soup = BeautifulSoup(detail_page_resp.text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
        print(title,'爬取成功!!!')

    fp.close()


if __name__ == '__main__':
    SpiderXiYou()