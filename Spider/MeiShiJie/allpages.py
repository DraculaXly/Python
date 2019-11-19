import singlepage as sp
import json

f = open('urls.json', 'r', encoding='utf-8')
data = json.loads(f.read(), encoding='utf-8')

if __name__ == "__main__":
    for i in range(len(data)):
        filename = data[i]['title']
        fileurl = data[i]['url']
        sp.get_single_page(filename, fileurl)