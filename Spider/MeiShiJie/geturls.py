'''
http://www.meishij.net/chufang/diy/
http://www.meishij.net/jiankang/
'''

from urllib import request
from lxml import etree
import json

f1 = open('urls.json', 'w', encoding='utf-8')
url = 'http://www.meishij.net/chufang/diy/'
response = request.urlopen(url)
result = response.read().decode('utf-8')
tree = etree.HTML(result)
category_list = tree.xpath('//*[@id="listnav_con_c"]/dl/dt/text()')

data = []
for i in range(len(category_list)):
    category_title = category_list[i]
    expression = '//*[@id="listnav_con_c"]/dl[' + str(i + 1) + ']/dd/a/text()'
    for j in range(len(tree.xpath(expression))):
        expression1 = '//*[@id="listnav_con_c"]/dl[' + str(i + 1) + ']/dd[' + str(j + 1) + ']/a/text()'
        expression2 = '//*[@id="listnav_con_c"]/dl[' + str(i + 1) + ']/dd[' + str(j + 1) + ']/a/@href'
        sub_category_title = tree.xpath(expression1)
        sub_category_url = tree.xpath(expression2)
        a = {'title': sub_category_title[0],'url': sub_category_url[0]}
        data.append(a)
json.dump(data, f1, ensure_ascii=False, indent=4)
f1.close()