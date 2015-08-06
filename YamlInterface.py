#encoding:utf-8
import yaml
from YamlStep import  YamlStep
from YamlHttpRequest import YamlHttpRequest
from YamlHttpResponse import YamlHttpResponse
from YamlVariable  import YamlVariable
import YamlDefault
import YamlHelper
from YamlTag import YamlTag

class YamlInterface():
    # 构造函数
    def __init__(self, yml_file_path):
        api = self.api_content(yml_file_path)

        # if api.has_key(YamlTag.Body) and api.has_key(YamlTag.Procedure):
        #     print "不允许同时配置Body和Procedure标签"
        #     return None

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
        for data_item in self.data_combination:
            self.request.invoke(data_item)


    # 排列组合
    def data_combine(self):
        # 将Yaml提供的字典类型转换成列表类型
        # 返回类型如：["name", ["value,", "value2", "value3"], ["password", ["value1", "value2", "value3"]]]
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
        res = lst[0]
        if len(lst) == 1:
            return res
        else:
            for i in range(1, len(lst)):
                res = self.assemble_dict_lst(res, lst[i])
        print res
        return res


    # lst的格式: ["name", ["value,", "value2", "value3"]]
    # 返回形如[{"name":"value1"}, {"name":"value2"}, {"name":"value3"}]
    def lst_dict_lst(self, lst):
        key = lst[0] # 列表第一个元素为key
        values = lst[1] # 列表第二个元素为一个列表，列举该key下的可选值
        return [{key: value} for value in values]


    # 将 [{"name":"value1"}, {"name":"value2"}, {"name":"value3"}]
    # 与 [{"password":"pass1"}, "password":"pass2"]
    # 两个列表进行排列组合成一个新的列表
    def assemble_dict_lst(self, src_lst, dst_lst):
        assemble_lst = []
        for src_dict in src_lst:
            for dst_dist in dst_lst:
                assemble_lst.append(dict(src_dict, **dst_dist))
        return assemble_lst


if __name__ == "__main__":
    interface = YamlInterface("interface.yml")
    interface.execute()
