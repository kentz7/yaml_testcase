#encoding:utf-8
import urllib2
import requests


class YamlHttpRequest():

    def __init__(self, url, auth, header, method, action):
        self.url = url
        self.auth = auth
        self.header = header
        self.method = method
        self.action = action


    # 调用请求
    def invoke(self, param_dict):
        try:
            print "HTTP请求URL: {0}".format(self.url + self.action)
            if self.method.upper() == "POST":
                response = requests.post(self.url + self.action, data=param_dict, headers=self.header)
            elif self.method.upper() == "GET":
                #response = requests.get(self.url + self.method, data=param_dict, headers=self.header)
                print "发送请求: {0}".format(self.url + self.action)
                print "发送参数: {0}".format(param_dict)
                print "Header: {0}".format(self.header)
                print "Auth: {0}".format(self.auth)
            elif self.method.upper() == "DELETE":
                response = requests.delete(host + method, data=param_dict, headers=headers)
            else:
                return None
            print "-" * 80
            #return response
        except urllib2.HTTPError, e:
            print "POST/GET请求出现错误！"
            print "POST/GET请求返回码: {0}".format(e.code)
            print "POST/GET请求结果: {0}".format(e.read())
            return None
