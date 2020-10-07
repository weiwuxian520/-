import requests
from lxml import etree

url = "https://www.aqistudy.cn/historydata/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
page_text = requests.get(url=url, headers=headers).text
allCity = []
# 数据解析
tree = etree.HTML(page_text)
# hot_city_tittle = tree.xpath('//div[@class="top"]/text()')[0]
# hot_city_list = tree.xpath('//div[@class="bottom"]/ul/li/a')#全部城市
# all_city_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li/a')#所有城市
all_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')

for li in all_list:
    allCityname = li.xpath('./text()')[0]
    allCity.append(allCityname)
    with open('city.csv', 'a+') as fp:
        fp.write(allCityname + '\n')

print("存储成功\n", allCity)

# print(hot_city_tittle,'\n',hot_city_list)
# all_city_tittle = tree.xpath('//div[@class="top"]/text()')[1]

# # print(all_city_tittle,'\n',all_city_list)


# for li in hot_city_list:
#     hot_city_name = li.xpath('./a/text()')[0]
#     all_hotCity.append(hot_city_name)
#     with open('city.csv', 'a+') as fp:
#         fp.write(hot_city_name+"\n")
#
# print(all_hotCity)
# print("存储成功")
