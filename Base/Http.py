__author__ = 'Administrator'
import urllib.request
import urllib.parse
import http.client
import time
HTTP = 'http://'
class http_request:
    def __init__(self, base_url='qixun.ckingiot.com', http_port=36882, http_api='/QiXunManager/index.php/Admin/Interface/UserLogin', method='post'):
        self.banse_url = base_url
        self.http_port = http_port
        self.http_api = http_api
        self.http_method = method
    def request(self, params=""):
        try:
            http_headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Connection': 'Keep-Alive',
                            'Referer': HTTP + self.banse_url, 'Accept': 'text/plain'}
            http_params = urllib.parse.urlencode(params)
            http_conn = http.client.HTTPConnection(self.banse_url)
            start_time = time.time()
            http_conn.request(method=self.http_method, url=self.http_api, body=http_params, headers=http_headers)
            http_response = http_conn.getresponse()
            print(HTTP + self.banse_url + self.http_api)
            if http_response.status == 200:
                print(time.time() - start_time)
                return time.time() - start_time
                #return http_response.read().decode('utf-8')
            else:
                print("请求失败")
                return False
        finally:
            http_conn.close()
