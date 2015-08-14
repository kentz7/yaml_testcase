#encoding:utf-8
import urllib2
import requests
from YamlTag import YamlTag


class YamlHttpRequest():

    def __init__(self, url, auth, header, method, action):
        self.url = url
        self.auth = (auth[YamlTag.Username], auth[YamlTag.Password]) if len(auth) > 0 else ()
        self.header = header
        self.method = method
        self.action = action


    # 调用请求
    def invoke(self, param_dict):
        try:
            print "HTTP URL: {0}".format(self.url + self.action)
            print "Parameter: {0}".format(param_dict)
            print "Header: {0}".format(self.header)
            print "Auth: {0}".format(self.auth)

            if self.method.upper() == "POST":
                response = requests.post(self.url + self.action, data=param_dict, headers=self.header, auth=self.auth)
            elif self.method.upper() == "GET":
                response = requests.get(self.url + self.method, data=param_dict, headers=self.header, auth=self.auth)
            elif self.method.upper() == "DELETE":
                response = requests.delete(host + method, data=param_dict, headers=headers, auth=self.auth)
            else:
                return None
            print u"HTTP 响应结果: {0}".format(response.text)
            print "-" * 120
            return response
        except urllib2.HTTPError, e:
            print u"POST/GET请求出现错误！"
            print u"POST/GET请求返回码: {0}".format(e.code)
            print u"POST/GET请求结果: {0}".format(e.read())
            return None
