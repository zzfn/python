import requests
from lxml import etree, html


# import lxml.html
#
# html = requests.get('https://anycloud.xyz').text
# lxml.
# print(html)
def run():
    # book = tree.xpath("body/div[@title='buyer-info']/child::*/text()")
    n = 1
    while True:
        url = 'http://econpy.pythonanywhere.com/ex/00' + str(n) + '.html'
        page = requests.get(url)
        if page.status_code == 404:
            break
        tree = etree.HTML(page.content.decode('utf8'))
        list = tree.xpath("body/div[@title='buyer-info']")
        print('第' + str(n) + '页')
        for i in range(1,len(list)):
            book = tree.xpath("body//div[@title='buyer-info'][" + str(i) + "]/div/text()")
            price = tree.xpath("body//div[@title='buyer-info'][" + str(i) + "]/span/text()")
            print(book[0],price[0])
        n += 1


if __name__ == "__main__":
    run()
