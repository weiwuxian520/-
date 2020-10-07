import requests
from lxml import etree
import os
def xiazai():
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    res = requests.get(url=url, headers=header)
    res.encoding = 'gbk'
    restext = res.text
    # 数据解析
    tree = etree.HTML(restext)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    if not os.path.exists('./美女'):
        os.mkdir('./美女')
    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        print(img_src, img_name)
        # 持久化存储
        img_data = requests.get(url=img_src, headers=header).content
        file_path = '美女/' + img_name
        with open(file_path, 'wb')as fp:
            fp.write(img_data)
            print(img_name, '下载成功')

for page in range(1,161):
    if page == 1:
        url = "http://pic.netbian.com/4kmeinv"
        xiazai()
    elif  page <=2:
        url = "http://pic.netbian.com/4kmeinv/index_" + str(page) + ".html"
        xiazai()
    else  :
        exit("退出成功")