#encoding:utf-8

import requests


class YamlHttpRequest():
    auth = {}
    header = {}
    url = ""
    method = ""
    action = ""
    params = {}

    def __init__(self, url, auth, header, method, action):
        self.url = url
        self.auth = auth
        self.header = header
        self.method = method
        self.action = action


    # 调用请求
    def invoke(self, param):
        pass
