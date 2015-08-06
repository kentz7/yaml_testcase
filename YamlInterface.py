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
    # YamlStep precondition
    # YamlStep procedure
    # YamlStep postcondition
    # YamlHttpRequest request
    # YamlHttpResponse response
    # YamlVariable variables
    # body = {}


    # 构造函数
    def __init__(self, yml_file_path):
        yml_file = open(yml_file_path)
        yml_dict = yaml.load(yml_file)
        api = yml_dict[YamlTag.Interface]

        Body = api[YamlTag.Body]
        Except = Body[YamlTag.Except]
        Auth = api[YamlTag.Auth]
        Method = api[YamlTag.Method]
        Global = api[YamlTag.Global]
        Precondition = api[YamlTag.Precondition]
        Procedure = api[YamlTag.Procedure]
        Postcondition = api[YamlTag.Postcondition]
        Url = api[YamlTag.Url]
        Header = api[YamlTag.Header]

        print Body
        print Except
        print Auth
        print Method
        print Global
        print Precondition
        print Procedure
        print Postcondition
        print Url
        print Header



    # 将Yaml提供的字典类型转换成列表类型
    # 返回类型如：["name", ["value,", "value2", "value3"], ["password", ["value1", "value2", "value3"]]]
    def yaml2lst(self,  yml_file_path):
        yml_file = open(yml_file_path)
        yml_dict = yaml.load(yml_file)


        return [[key, form_data[key]["values"]] for key in form_data]



    def lst_dict_lst(self, lst):
        # lst的格式: ["name", ["value,", "value2", "value3"]]
        # 返回形如[{"name":"value1"}, {"name":"value2"}, {"name":"value3"}]
        key = lst[0] # 列表第一个元素为key
        values = lst[1] # 列表第二个元素为一个列表，列举该key下的可选值
        return [{key: value} for value in values]


    # 将 [{"name":"value1"}, {"name":"value2"}, {"name":"value3"}]
    # 与 [{"password":"pass1"}, "password":"pass2"]
    # 两个列表进行排列组合成一个新的列表
    def assemble_dict_lst(src_lst, dst_lst):
        assemble_lst = []
        for src_dict in src_lst:
            for dst_dist in dst_lst:
                assemble_lst.append(dict(src_dict, **dst_dist))
        return assemble_lst


    # 排列组合
    def data_combination(form_data):
        lst = [lst_dict_lst(item) for item in yaml_dict2list(form_data)]
        res = lst[0]
        if len(lst) == 1:
            return res
        else:
            for i in range(1, len(lst)):
                res = assemble_dict_lst(res, lst[i])
        return res


if __name__ == "__main__":
    YamlInterface("interface.yml")
