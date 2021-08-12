# coding utf -8

import time
import requests
from threading import Thread


class Cl(object):
    def __init__(self, url, params):
        self.url = url
        self.params = params

    def log_url(self):
        global ERROR_NUM
        try:
            r = requests.request('get', self.url, params=self.params)
            print(r.text)
        except Exception as e:
            print(e)
            ERROR_NUM += 1

    def run(self):
        """一个线程执行多少次任务"""
        i = 0
        while i < ONE_WORKER_NUM:
            i += 1
            self.log_url()
            time.sleep(LOOP_SLEEP)
            print(i)

    def runs(self):
        """开启多个线程执行任务"""
        t1 = time.time()
        Threads = []
        Two_Threads = []
        for i in range(THREAD_NUM):
            t = Thread(self.run(), name='t'+str(i))
            t_two = Thread(self.run(), name='t_two'+str(i))
            t.setDaemon(True)
            t_two.setDaemon(True)
            Threads.append(t)
            Two_Threads.append(t_two)

            t.start()
            t_two.start()

        # for t in Threads:
        #     t.start()
        # for two in Two_Threads:
        #     two.start()

        for t in Threads:
            """子线程结束后主线程在结束"""
            t.join()
        for two in Two_Threads:
            two.join()

        t2 = time.time()
        print("===============压测结果===================")
        print("URL:", self.url)
        print("任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM)
        print("总耗时(秒):", t2 - t1)
        print("每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
        print("每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
        print("错误数量:", ERROR_NUM)


if __name__ == '__main__':
    url = 'http://192.168.90.101/sso-auth/rest/sso/login'
    params = {
        'username': 'system',
        'password': '12345678',
        'service': 'http://192.168.90.162:8090/ims-pro/',
        'action': 'login',
        'rememberMe': 'false',
        'callback': 'beyond_callback_15'
    }
    ERROR_NUM = 0  # 出错数
    THREAD_NUM = 2  # 并发线程总数
    ONE_WORKER_NUM = 5  # 每个线程的循环次数
    LOOP_SLEEP = 1  # 每次请求时间间隔(秒)

    obj = Cl(url, params)
    obj.runs()
