#从标签中取出文本内容
from bs4 import BeautifulSoup
fp = open('test1.html', encoding = 'utf-8')
soup = BeautifulSoup(fp, 'lxml')
print(soup.select('.first')[1].string)
print(soup.select('.first')[1].text)
#从标签中取出属性
from bs4 import BeautifulSoup
fp = open('test1.html', encoding = 'utf-8')
soup = BeautifulSoup(fp, 'lxml')
print(soup.find(class_ = 'first')['class'])
