import requests
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1587292481371&di=a47137f669670075ec1049a5738eb657&imgtype=0&src=http%3A%2F%2Fbbs.jooyoo.net%2Fattachment%2FMon_0905%2F24_65548_2835f8eaa933ff6.jpg'
response = requests.get(url = url)
content = response.content
with open('图片.jpg', 'wb') as fp:
    fp.write(content)