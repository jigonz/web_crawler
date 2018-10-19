import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'https://dallas.craigslist.org/search/mca?s=120'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class', 'result-title hdrlnk'}):
            href = link.get('href')
            title = link.string
            print(href)
            #print(title)
            get_single_item_data(href)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('span', {'class', 'price'}):
        print(item_name.string)
    #for link in soup.findAll('a'):
     #   href = link.get('href')
      #  print(href)

trade_spider(2)