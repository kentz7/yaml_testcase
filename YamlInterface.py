#encoding:utf-8
import yaml
from YamlStep import  YamlStep
from YamlHttpRequest import YamlHttpRequest
from YamlHttpResponse import YamlHttpResponse
from YamlVariable  import YamlVariable
import YamlDefault
import YamlHelper
from YamlTag import YamlTag
import os
import json

class YamlInterface():
    # 构造函数
    def __init__(self, yml_file_path):
        api = self.api_content(yml_file_path)

        # if api.has_key(YamlTag.Body) and api.has_key(YamlTag.Procedure):
        #     print "不允许同时配置Body和Procedure标签"
        #     return None

        # Yml 文件名及输出结果的路径
        file_name = os.path.split(yml_file_path)[1]
        root_dir = YamlHelper.same_prefix(os.path.abspath(yml_file_path), os.getcwd())
        self.interface_name = file_name[0:file_name.index(".")]
        self.response_file = "{0}/response/{1}.yml".format(root_dir, self.interface_name)

        # Yaml请求
        self.request = YamlHttpRequest(YamlHelper.http_option(api, YamlTag.Url),
                                       YamlHelper.http_option(api, YamlTag.Auth),
                                       YamlHelper.http_option(api, YamlTag.Header),
                                       YamlHelper.http_option(api, YamlTag.Method),
                                       YamlHelper.http_option(api, YamlTag.Action))
        # 请求的主体
        self.body = api[YamlTag.Body]

        # 前置操作
        self.precondition = YamlStep()

        # 执行过程 -- 为避免与body重复，可考虑不要该标签
        # self.procedure = YamlStep()

        # 后置操作
        self.postcondition = YamlStep()

        # 全局变量
        self.variables = YamlVariable()

        # 参数数据组合
        self.data_combination = self.data_combine()


    # 获取接口详情内容
    def api_content(self, yml_file_path):
        yml_file = open(yml_file_path)
        yml_dict = yaml.load(yml_file)
        return yml_dict[YamlTag.Interface]


    # 发送请求
    def execute(self):
        print "开始执行接口用例"
        # 遍历所有数组合发送所有的HTTP请求
        for data_item in self.data_combination:
            response = self.request.invoke(data_item)
            self.save_check_response(data_item, response)


    # 保存请求记录
    def save_check_response(self, data_item, response):
        # 先判断文件夹和文件是否存在
        if not os.path.exists(self.response_file):
            if not os.path.exists(os.path.split(self.response_file)[0]):
                os.makedirs(os.path.split(self.response_file)[0])
            res_file = open(self.response_file, "w")
            res_file.close()

        # 读写文件
        # 如果已经存在该配置了，则忽略
        old_yml_dict = yaml.load(open(self.response_file, "r"))
        response_dict = yaml.load(response.text)
        res_file = open(self.response_file, "a")


        # 获取key值，由于dict具有无序性，再创建key时需要以key做一次排序
        key_str = "key_"
        # iteritems() 返回一个字典键值对的元组集合
        sorted_data_item = sorted(data_item.iteritems(), key=lambda k:k[0], reverse=False)
        for item in sorted_data_item:
            key_str = key_str + str(item[1]) + "_"
        key_str = key_str[0:len(key_str)-1]

        result_dict = {}
        # 先要判断key是否存在，如果存在则不做任何处理，不存在则插入
        if (old_yml_dict is None) or (not old_yml_dict.has_key(key_str)):
            print "插入新的key: {0}".format(key_str)
            result_dict[key_str] = data_item
            result_dict[key_str][YamlTag.Response] = response_dict
            yaml.dump(result_dict, res_file, default_flow_style=False, indent=4)
            res_file.write("\n")
        else:
            print "已经存在key: {0}".format(key_str)
            print "已存在的key的内容为: {0}".format(old_yml_dict[key_str][YamlTag.Response])
            # 存在该Key，就需要去比较该key的值和response的值
            # 比较 old_yml_dict[YamlTag.Response] 与 response_dict 的值，以old_yml_dict为准
            flag = YamlHelper.left_cmp_dict(old_yml_dict[key_str][YamlTag.Response], response_dict)
        res_file.close()
        return flag


    # 排列组合
    def data_combine(self):
        # 将Yaml提供的字典类型转换成列表类型
        # yamlLst格式如: ["name", ["value,", "value2", "value3"], ["password", ["value1", "value2", "value3"]]]
        yamlLst = []
        for key in self.body:
            if self.body[key].has_key(YamlTag.Values):
                # 如果有values标签，则使用该标签
                values = self.body[key][YamlTag.Values]
            else:
                # 没有values标签，则使用该类型下的默认值
                value_type = self.body[key][YamlTag.Type]
                values = YamlHelper.yaml_default(value_type)
            yamlLst.append([key, values])


        lst = [self.lst_dict_lst(item) for item in yamlLst]
        dc = lst[0]
        if len(lst) == 1:
            return dc
        else:
            for i in range(1, len(lst)):
                dc = self.assemble_dict_lst(dc, lst[i])
        return dc


    # lst的格式: ["name", ["value,", "value2", "value3"]]
    # 返回形如: [{"name":"value1"}, {"name":"value2"}, {"name":"value3"}]
    def lst_dict_lst(self, lst):
        key = lst[0] # 列表第一个元素为key
        values = lst[1] # 列表第二个元素为一个列表，列举该key下的可选值
        return [{key: value} for value in values]


    # 将 [{"name":"value1"}, {"name":"value2"}, {"name":"value3"}]
    # 与 [{"password":"pass1"}, {"password":"pass2"}]
    # 两个列表进行排列组合成一个新的列表
    def assemble_dict_lst(self, src_lst, dst_lst):
        assemble_lst = []
        for src_dict in src_lst:
            for dst_dist in dst_lst:
                assemble_lst.append(dict(src_dict, **dst_dist))
        return assemble_lst


if __name__ == "__main__":
    interface = YamlInterface("interface/user_login.yml")
    # for item in interface.data_combination:
    #     print item
    interface.execute()
