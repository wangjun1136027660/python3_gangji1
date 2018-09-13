from bs4 import BeautifulSoup
import requests,time
# import time
import pymongo
# import random


client = pymongo.MongoClient('localhost', 27017)
ganji1 = client['ganji1']
url_list = ganji1['url_list']
item_info = ganji1['item_info']

headers  = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Connection':'keep-alive'
}

# http://cn-proxy.com/
# proxy_list = [
#     'http://117.177.250.151:8081',
#     'http://111.85.219.250:3129',
#     'http://122.70.183.138:8118',
#     ]
# proxy_ip = random.choice(proxy_list) # 随机获取代理ip
# proxies = {'http': proxy_ip}



# spider 1
# ================================== <<获取每个个人卖家的网店链接,做了剔除末页处理>> ========================================
def get_links_from(channel, pages, who_sells='o'):
    # http://bj.ganji.com/ershoubijibendiannao/o3/
    # o for personal a for merchant
    # time.sleep(1)
    try:
        list_view = '{}{}{}/'.format(channel, who_sells, str(pages))
        # time.sleep(1)
        wb_data = requests.get(list_view,headers=headers,timeout = 20000) # get 方法的一系列 参数-,proxies=proxies
        soup = BeautifulSoup(wb_data.text, 'lxml')
        if len(soup.select('td.t')) >= 10: # 仔细分析网页，得出的结论！
            for link in soup.select('td.t a'):
                if link.get('data-jingzhunurl') == None : # 剔除精品 栏目！  and link.get('div.noinfotishi') == None
                    item_link0 = link.get('href').split('?')[0]
                    if item_link0[:4] != 'http': # 剔除不标准，url字符串
                        item_link='http:'+item_link0
                        url_list.insert_one({'url': item_link})
                    else:
                        url_list.insert_one({'url': item_link0})
                    # print(item_link)
                else:
                    pass
        else:
            pass
    except TimeoutError:
        pass
# ======================================================== >>

# spider 2
# ===================================== <<获取详情页的信息，做了剔除了失效页面 处理！>> =====================================
def get_item_info_from(url,data=None):
    # time.sleep(1)
    try:
        wb_data = requests.get(url,headers=headers,timeout = 20000)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        if soup.find('span','soldout_btn') : # 剔除，商品已经下架的页面。
            pass
        else:
            data = {
                'title':soup.select('h1.info_titile')[0].get_text(),
                'price':soup.select('span.price_now i')[0].get_text(),
                'seller_name':soup.select('p.personal_name')[0].get_text(),
                'area':soup.select('div.palce_li i')[0].get_text(),
                'cates':list(soup.select('div.biaoqian_li')[0].stripped_strings), # 多标签的处理方法
                'url':url
            }
            item_info.insert_one(data)
            # print('个体商户，详情已录入！')
    except (TimeoutError,IndexError):
        pass


# get_item_info_from('http://zhuanzhuan.ganji.com/detail/950914651580547083z.shtml')
# get_links_from('http://bj.ganji.com/shouji/',2)
