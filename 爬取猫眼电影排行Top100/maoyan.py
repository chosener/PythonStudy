import json
import time
import requests
import re


def get_one_page(url):
    # cookie会随着时间变动,因为网站有滑动验证码
    headres = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'Referer': 'https://www.maoyan.com/board/4?timeStamp=1640745691361&channelId=40011&index=8&signKey=ab1b0f6f4e3b78e844ff5b244cf8d1ad&sVersion=1&webdriver=false',
        'Host': 'www.maoyan.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cookie': '__mta=208034733.1640745595080.1640830616526.1640830631009.17; uuid_n_v=v1; uuid=9B0A0400685011EC87FF41B5867757989FC77C68374F455580CDEF5A5CC9CC9B; _lxsdk_cuid=17e040ef0b0c8-033d62ba2f4e9f-b7a1a38-144000-17e040ef0b0c8; _lxsdk=9B0A0400685011EC87FF41B5867757989FC77C68374F455580CDEF5A5CC9CC9B; _csrf=ce95791eacf6b9d18234b4edcafb962359227c962e94ed6659faa515eff3e83a; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1640745595,1640830596; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1640830631; _lxsdk_s=17e091ff25f-d59-a3d-ddc%7C%7C8'
    }


    # 创建会话，建立连接
    S = requests.session()
    req = requests.Request('GET', url, headers=headres)
    pre = S.prepare_request(req)
    response = S.send(pre)
    if (response.status_code == 200):
        text = response.text
        # 用正则化进行匹配
        pattern_total = '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>上映时间：(.*?)</p>'
        # 利用findall匹配所有
        pattern = re.compile(pattern_total, re.S)
        items = re.findall(pattern, text)
        for item in items:
            yield {
                'index': item[0],
                'img': item[1],
                'name': item[2],
                'actors': item[3].strip()[3:] if len(item[3]) > 3 else " ",
                'releasetime': item[4]
            }
    else:
        print(response.status_code)


# 写入文件为json格式,text为一个字典
def write_into(text):
    with open("result.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(text, ensure_ascii=False) + "\n")


if __name__ == '__main__':
    # 分页爬取，页数与offset有关
    for n in range(10):
        time.sleep(1)
        url = 'https://www.maoyan.com/board/4?requestCode=7f63ee590fdbcb3208b59ab53a9c2144u20ol&offset=' + str(10 * n)
        res = get_one_page(url)
        for item in res:
            write_into(item)

