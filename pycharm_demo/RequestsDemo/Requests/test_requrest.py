import requests


class TestRequrst:

    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get', )
        print(r.json())

    def test_post(self):
        payload = {
            "name": 'zhang',
            "level": 1
        }
        r = requests.post('https://httpbin.testing-studio.com/post', params=payload)
        print(r.json())

    # cookie处理 可以定制请求头
    def test_cookies(self):
        header = {
            "Cookie": "hogwarts=school",
            'User-Agent': 'hogwarts'
        }
        r = requests.post('https://httpbin.testing-studio.com/cookies', headers=header)
        print(r.request.headers)

    # 以参数的方式传递cookie
    def test_cookies_demo(self):
        header = {
            'User-Agent': 'hogwarts'
        }
        cookie_date = {
            "Cookie": "school1",
            "test": "AD"
        }
        r = requests.post('https://httpbin.testing-studio.com/cookies', headers=header, cookies=cookie_date)
        print(r.request.headers)

    def test_send(self):
        date = {
            "method": "get",
            "url": "http://192.168.90.162:9000/rpt-company/rectifys/list?pageNum=1&pageSize=10&orderType=2",
            "header": {
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50SWQiOiI5NSIsInN1YiI6Iuays-WNl-WGnOadkeWuoui_kOS8geS4muerryIsImFyZWFDb2RlIjoiNDExNjAyIiwiY29tcGFueUlkIjoiNDExNjAyMDAwMDAwMDQ3MSIsImNvbXBhbnlOYW1lIjoi5ZGo5Y-j5biC5rG96L2m6L-Q6L6T6ZuG5Zui6YCa5a6H6LSn6L-Q5pyJ6ZmQ5YWs5Y-4IiwiaWF0IjoxNjM5NTM0NjM4LCJhY2NvdW50IjoiNDExNjAxMDAwNTAxLTI1In0.2MfUWgBi4TKa3vs6pdgTPl7WOfZnvTMZm3-mYJWnJbM"}
        }
        r = requests.request(method=date["method"], url=date["url"], headers=date["header"])
        print(r.json())
        print(r.request.headers)
