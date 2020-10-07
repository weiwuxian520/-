import scrapy


class QiushiSpider(scrapy.Spider):
    # 爬虫文件的名称：就是爬虫源文件的一个唯一标识
    name = 'qiushi'
    # 允许的域名：用来限定start——urls列表中哪些url可以进行请求发送
    # allowed_domains = ['https://www.qiushibaike.com/']
    # 起始的url列表：该列表中存放的url会被scrapy自动进行请求的发送，可以有多个链接，逗号隔开
    start_urls = ['https://qiushibaike.com/text/']

    # 用作数据解析：response参数标示的就是请求成功后对应的响应对象
    def parse(self, response):
        # 解析：作者的名称+段子内容
        div_list = response.xpath('//div[@class = "col1 old-style-col1"]/div')
        for div in div_list:
            author = div.xpath('.//div[@class = "author clearfix"]/a[2]/h2/text()').extract_first()
            content = div.xpath('.//div[@class = "content"]/span//text()').extract()
            content = ''.join(content)
            print(author, content)