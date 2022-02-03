#findall()函数
import requests
import re
url = 'https://www.cnblogs.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
response = requests.get(url = url, headers = headers).text
ex = '<div class="post_item_body">.*?target="_blank">(.*?)</a></h3>'
print(re.findall(ex,response,re.S))
#search()函数
import re
str1 = '123Qwe!_@#你我他'
ret = re.search('\w', str1)
print(ret.group())
#finditerr()函数
import re
str1 = '123Qwe!_@#你我他'
ret = re.finditer('\w', str1)
for i in ret:
    print(i.group(),end = '')
