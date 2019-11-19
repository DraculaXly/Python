'''
get one page information
'''

from urllib import request
from lxml import etree
import json
import re

def get_single_page(f_name, f_url):
    url = f_url
    response = request.urlopen(url)
    result = response.read().decode('utf-8')
    tree = etree.HTML(result)
    try:
        totalpages = tree.xpath('//*[@id="listtyle1_w"]/div[2]/div/span[2]/form/text()[1]')
        totalpagesnumberlist = re.findall('[0-9]\d*', totalpages[0])
        totalpagesnumber = totalpagesnumberlist[0]
    except Exception:
        pass

    filename = f_name + '.json'
    f1 = open(filename, 'w', encoding='utf-8')
    data = []
    try:
        for i in range(1, int(totalpagesnumber) + 1):
            url1 = f_url + '?&page=' + str(i)
            response1 = request.urlopen(url1)
            result1 = response1.read().decode('utf-8')
            tree1 = etree.HTML(result1)
            itemlist = tree1.xpath('//*[@id="listtyle1_list"]/div/@class')
            for i in range(1, len(itemlist) + 1):
                str1 = '//*[@id="listtyle1_list"]/div[' + str(i) + ']/a/div/div/div[1]/strong/text()'
                str2 = '//*[@id="listtyle1_list"]/div[' + str(i) + ']/a/img/@src'
                str3 = '//*[@id="listtyle1_list"]/div[' + str(i) + ']/a/@href'
                item_title = tree1.xpath(str1)
                item_img = tree1.xpath(str2)
                item_make = tree1.xpath(str3)
                a = {
                    'title': item_title[0],
                    'image': item_img[0],
                    'make': item_make[0]
                    }
                data.append(a)
    except Exception:
        pass
    json.dump(data, f1, ensure_ascii=False, indent=4)
    f1.close()