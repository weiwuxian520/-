import requests
import re
import os
#创建一个文件夹
if not os.path.exists('./qiutu'):
    os.mkdir('./qiutu')

url="https://www.qiushibaike.com/imgrank/"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

res = requests.get(url=url,headers=header).text
#写一个正则来匹配包含有图片路径的标签
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
img_src_list = re.findall(ex,res,re.S)
print(img_src_list)
for src in img_src_list:
#拼接一个完整的图片url
    src = 'https:'+ src
#请求到图片的二进制数据
    image_data=requests.get(url=url,headers=header).content
#生成图片名称
    img_name = src.split('/')[-1]
#图片存储的路径
    imgPath = './qiutu/'+img_name

    with open(imgPath,'wb')as fp:
        fp.write(image_data)
        print(img_name,'下载成功')
