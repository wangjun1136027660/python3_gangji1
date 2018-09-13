from multiprocessing import Pool
from page_parsing import get_item_info_from,url_list,item_info,get_links_from
from channel_extracing import url_list0

db_urls = [item['url'] for item in url_list.find()]
index_urls = [item['url'] for item in item_info.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x-y

def get_all_links_from(channel):
    try:
        for i in range(1,100):
            get_links_from(channel,i)
    except TimeoutError:
        pass


if __name__ == '__main__':
    l=[]
    pool = Pool()
    # pool = Pool()
    # for x in url_list0.find():
    #     l.append(x['http'])
    pool.map(get_item_info_from,rest_of_urls)
    pool.close()
    pool.join()



