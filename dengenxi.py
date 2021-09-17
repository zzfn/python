import requests
import json


def get_containerid(url):
    res = requests.get(url)
    content = json.loads(res.content).get("data")
    for data in content.get('tabsInfo').get('tabs'):
        if data.get('tab_type') == 'weibo':
            containerid = data.get('containerid')
    return containerid


def get_user_info(uid):
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + uid
    res = requests.get(url)
    content = json.loads(res.content)
    user_info = content['data']['userInfo']
    print('用户名：' + user_info.get('screen_name'))
    return


def get_user_content(uid):
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + uid
    i = 1
    containerid = get_containerid(url)
    while True:
        weibo_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + uid + '&containerid=' + containerid + '&page=' + str(
            i)
        print(weibo_url)
        try:
            data = requests.get(weibo_url).content
            content = json.loads(data).get('data')
            cards = content.get('cards')
            if len(cards) != 0:
                for j in range(len(cards)):
                    print("第" + str(i) + "页，第" + str(j) + "条")
                    mblog = cards[j].get('mblog')
                    if str(mblog).find('retweeted_status') == -1:
                        if str(mblog).find('original_pic') != -1:
                            list_url = mblog.get('pics')
                            for url in list_url:
                                n = 0
                                path = str(i) + '-' + str(j) + '-' + str(n)
                                img_url = url.get('large').get('url')
                                print('第' + str(n) + '张', end='')
                                with open("/Users/chenchen/Desktop/me/python/dex/" + path + img_url[-4:], 'wb') as f:
                                    f.write(requests.get(url.get('large').get('url')).content)
                                print('...OK!')
                                n = n + 1
                i += 1
        except Exception as e:
            print(e)
            pass


get_user_content("3942274365")