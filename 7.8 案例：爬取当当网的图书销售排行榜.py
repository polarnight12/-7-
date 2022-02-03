import requests
import pandas as pd
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

data_info = {'图书排名': [], '图书名称': [], '图书作者': [], '图书出版时间': [], '图书出版社': [], '图书价格': []}
def parse_html(soup):
    li_list = soup.select('.bang_list li')
    for li in li_list:
        data_info['图书排名'].append(li.select('.list_num ')[0].text.replace('.', ''))
        data_info['图书名称'].append(li.select('.name a')[0].text)
        data_info['图书作者'].append(li.select('.publisher_info ')[0].select('a')[0].text)
        data_info['图书出版时间'].append(li.select('.publisher_info span')[0].text)
        data_info['图书出版社'].append(li.select('.publisher_info ')[1].select('a')[0].text)
        data_info['图书价格'].append(float(li.select('.price  .price_n')[0].text.replace('¥', '')))

for i in range(1, 26):
    url = f'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-{i}'
    response = requests.get(url = url, headers = headers, timeout = 10)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')
    parse_html(soup)
    print(f'第{i}页爬取完毕')

book_info = pd.DataFrame(data_info)
print(book_info.isnull())
print(book_info.duplicated())

book_info['图书价格'][book_info['图书价格'] > 100] = None
book_info = book_info.dropna()

book_info.to_csv('当当网图书销售排行.csv', encoding = 'utf-8', index = False)