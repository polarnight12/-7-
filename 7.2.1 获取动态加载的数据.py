import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
url = 'https://movie.douban.com/j/chart/top_list'
params = {'type': '25', 'interval_id': '100:90', 'action': '', 'start': '0', 'limit': '1'}
response = requests.get(url, headers = headers, params = params)
print(response.json())