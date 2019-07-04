import random
import urllib.request
import json
import re
# 定义要爬取的微博大V的微博ID
import requests
import time

iplist = ['60.13.42.8:9999', '117.90.0.172:9000', '121.232.148.156:9000', '120.234.138.99:53779', '120.79.64.147:8118']

proxy_addr = "60.11.5.104:80"

id = '1621323850'


# 定义页面打开函数
def use_proxy(url, proxy_addr):
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    req.add_header("cookie",
                   "ALF=1563501151; SCF=Apx1PRwrfB4If6VYDuCoe_oorlZ5gXCWgirtv_8vjRInbSiwiRjXJzR1HlwIwMRHub8Qq-MsnmzwbCu94WX7vlA.; SUB=_2A25wDe0fDeRhGeVH71AT9yrPzTmIHXVT8fNXrDV6PUJbktANLWrRkW1NT0BnhRvEpps1o8r4U5Lq6WlEI11t3hu5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhgALk5OZhvyM8uOfTuxHgy5JpX5K-hUgL.Foe4ShzES0B0So-2dJLoIpjLxKnLB.BLB-qLxK-LBK-LBoqLxKML1h.L1-zt; SUHB=0idrAQnnVzMAp9; MLOGIN=1; _T_WM=62061002588; WEIBOCN_FROM=1110006030; XSRF-TOKEN=afb963; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1005051353112775%26oid%3D4244627785851269%26fid%3D1078031353112775%26uicode%3D10000011")
    proxy = urllib.request.ProxyHandler({'http': random.choice(iplist)})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    return data


# 获取微博大V账号的用户基本信息，如：微博昵称、微博地址、微博头像、关注人数、粉丝数、性别、等级等
def get_userInfo(id):
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id
    data = use_proxy(url, random.choice(iplist))
    content = json.loads(data).get('data')
    profile_image_url = content.get('userInfo').get('profile_image_url')
    description = content.get('userInfo').get('description')
    profile_url = content.get('userInfo').get('profile_url')
    verified = content.get('userInfo').get('verified')
    guanzhu = content.get('userInfo').get('follow_count')
    name = content.get('userInfo').get('screen_name')
    na = name
    fensi = content.get('userInfo').get('followers_count')
    gender = content.get('userInfo').get('gender')
    urank = content.get('userInfo').get('urank')
    print("微博昵称：" + name + "\n" + "微博主页地址：" + profile_url + "\n" + "微博头像地址：" + profile_image_url + "\n" + "是否认证：" + str(
        verified) + "\n" + "微博说明：" + description + "\n" + "关注人数：" + str(guanzhu) + "\n" + "粉丝数：" + str(
        fensi) + "\n" + "性别：" + gender + "\n" + "微博等级：" + str(urank) + "\n")


def download():
    i = 1
    all=0
    Directory = 'C:\zhangzimu\MM\\'
    while True:
        url = 'https://m.weibo.cn/api/container/getSecond?containerid=1078031621323850_-_photoall&page=' + str(i)
        data = use_proxy(url, random.choice(iplist))
        content = json.loads(data).get('data')
        cards = content.get('cards')
        if(len(cards)>0):
            for j in range(len(cards)):
                pics = cards[j].get('pics')
                if(len(pics)>0):
                    for k in range(len(pics)):
                        pic_big = pics[k].get('pic_big')
                        all+=1
                        print("第"+str(i)+"页-----第"+str(k)+"个")
                        print(pic_big)
                        with open(Directory + str(i)+"-"+str(j)+"-"+str(k)+"-"+str(all)+".jpg", 'wb') as f:
                            f.write(requests.get(pic_big).content)
                        print("共"+str(all))
            i+=1
if __name__ == "__main__":
    get_userInfo(id)
    download()
