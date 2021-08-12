
import requests
import http.client
import json

ls = {'act':'list'}
url = 'https://app.topws.cn/index.php?url=user/signin&name=15671278825&password=sjq123456'
conn = http.client.HTTPConnection('hz.topws.cn')
conn.request(method='GET', url=url)
response = conn.getresponse()
res = response.read()
# rs = json.loads(res)
print(res)
