import requests
from lxml import etree
#爬去58二手房的相关信息

url = "https://bj.58.com/ershoufang/"
header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
#获取页面源码数据
res = requests.get(url=url,headers=header).text
#数据解析
tree = etree.HTML(res)
li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
for li in li_list:
    title = li.xpath('./div[2]/h2/a/text()')[0]
    print(title,'\n')
    with open('房源信息.csv','a+') as fp:
        fp.write(title+'\n')