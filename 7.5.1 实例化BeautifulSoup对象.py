#使用bs4模块中的BeautifulSoup类实例化对象
from bs4 import BeautifulSoup
fp = open('test1.html', encoding = 'utf-8')
soup = BeautifulSoup(fp, 'lxml')
#将爬取到的页面源码实例化成BeautifulSoup对象
from bs4 import BeautifulSoup
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
response = requests.get(url = 'https://www.baidu.com', headers = headers ).text
soup = BeautifulSoup(response, 'lxml')
