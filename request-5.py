import requests
import json
url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList"
header= {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
id_list = []  # 存储企业的id
all_comp_list = []  # 存储所有企业的数据

for page in range(1,7):
    page =str(page)
    data = {
            "on": "true",
            "page": page,
            "pageSize": '15',
            "productName":" ",
            "conditionType": "1",
            "applyname": "",
            "applysn": ""
        }
    json_ids = requests.post(url=url,data=data,headers=header).json()
    #遍历当前的json信息里的list对应的value值里ID，list是个字典
    for dic in json_ids['list']:
        id_list.append(dic['ID'])
    print(id_list)#打印当前数组里存储的企业id
post_url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById"
#开始拼接链接
for id in id_list:
    data = {
        'id' : id
    }
compnylist = requests.post(url=post_url, data=data,headers=header).json()
all_comp_list.append(compnylist)

fn = "化妆品.txt"
fp = open(fn,'a+',encoding='utf-8')
json.dump(all_comp_list,fp=fp,ensure_ascii=False)


