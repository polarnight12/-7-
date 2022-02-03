#通过标签名进行定位
from bs4 import BeautifulSoup
fp = open('test1.html', encoding = 'utf-8')  # 读取Html文档
soup = BeautifulSoup(fp, 'lxml')  # 实例化对象
print(soup.p)
#通过标签属性进行定位
from bs4 import BeautifulSoup
fp = open('test1.html', encoding = 'utf-8')
soup = BeautifulSoup(fp, 'lxml')
print(soup.find(class_ = 'first'))
print(soup.find_all(class_ = 'first'))
#通过标签名+标签属性进行定位
from bs4 import BeautifulSoup
fp = open('test1.html', encoding = 'utf-8')
soup = BeautifulSoup(fp, 'lxml')
print(soup.find('div', class_ = 'first'))
print(soup.find_all('div', class_ = 'first'))
#通过选择器进行定位
from bs4 import BeautifulSoup
fp = open('test1.html', encoding = 'utf-8')
soup = BeautifulSoup(fp, 'lxml')
print(soup.select('#first'))

from bs4 import BeautifulSoup
fp = open('test1.html', encoding = 'utf-8')
soup = BeautifulSoup(fp, 'lxml')
print(soup.select('.first'))

from bs4 import BeautifulSoup
fp = open('test1.html', encoding = 'utf-8')
soup = BeautifulSoup(fp, 'lxml')
print(soup.select('li'))

from bs4 import BeautifulSoup
fp = open('test1.html', encoding = 'utf-8')
soup = BeautifulSoup(fp, 'lxml')
print(soup.select('div>ul>#first'))
print(soup.select('div>ul>li'))
print(soup.select('div li'))
