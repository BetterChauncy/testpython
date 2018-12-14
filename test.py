import requests
from bs4 import BeautifulSoup
import os
import uuid

if not os.path.exists("E:\MyDownloads"):
    os.mkdir("E:\MyDownloads")

for page in range(1, 85):
    url = 'https://bing.ioliu.cn/?p=' + str(page)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # print(url)
    r = requests.get(url, headers=headers)
    contents = r.text

    soup = BeautifulSoup(contents, 'html.parser')
    divs = soup.find_all('div', 'item')

    for div in divs:
        imgs = div.find_all('img')
        for img in imgs:
            replace = img['src'].replace("400x240", "1920x1080")
            print(replace)
            res = requests.get(replace, headers=headers)
            with open('E:\MyDownloads\%s.jpg' % uuid.uuid1(), 'wb') as file:
                file.write(res.content)
