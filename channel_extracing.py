from bs4 import BeautifulSoup
import requests,pymongo

client = pymongo.MongoClient('localhost', 27017)
ganji1 = client['ganji1']
url_list0 = ganji1['url_list0']

start_url = 'http://bj.ganji.com/wu/' # 赶集，二手子网页 url
url_host = 'http://bj.ganji.com' # 用于构造，新的url

# ============================================= <获取商品大类链接，的函数> ================================================
def get_index_url(url):
    # url = start_url
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('dl.fenlei dt a') # select 返回一个 [list] ,   <...> ... <...>
    for link in links:
        page_url = url_host + link.get('href')
        url_list0.insert_one({'http':page_url})
    print('已获取所有大类网页链接！')
# ==============================================================
# get_index_url(start_url)

channel_list = '''
http://bj.ganji.com/jiaju/
http://bj.ganji.com/rirongbaihuo/
http://bj.ganji.com/shouji/
http://bj.ganji.com/bangong/
http://bj.ganji.com/nongyongpin/
http://bj.ganji.com/jiadian/
http://bj.ganji.com/ershoubijibendiannao/
http://bj.ganji.com/ruanjiantushu/
http://bj.ganji.com/yingyouyunfu/
http://bj.ganji.com/diannao/
http://bj.ganji.com/xianzhilipin/
http://bj.ganji.com/fushixiaobaxuemao/
http://bj.ganji.com/meironghuazhuang/
http://bj.ganji.com/shuma/
http://bj.ganji.com/laonianyongpin/
http://bj.ganji.com/xuniwupin/
http://bj.ganji.com/qitawupin/
http://bj.ganji.com/ershoufree/
http://bj.ganji.com/wupinjiaohuan/
'''

