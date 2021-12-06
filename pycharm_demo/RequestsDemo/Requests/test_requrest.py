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
