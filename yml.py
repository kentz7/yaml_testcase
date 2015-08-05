#encoding:utf-8
import yaml

def wrap_lst(lst):
    # 格式 ["name", ["value,", "value2", "value3"]]
    key = lst[0] # 列表第一个元素为key
    values = lst[1] # 列表第二个元素为一个列表，列举该key下的可选值
    # 返回形如[{"name":"value1"}, {"name":"value2"}, {"name":"value3"}]
    return [{key: value} for value in values]


# 将 [{"name":"value1"}, {"name":"value2"}, {"name":"value3"}]
# 与 [{"password":"pass1"}, "password":"pass2"]
# 两个列表进行排列组合成一个新的列表
def assemble_wrap_lst(src_lst, dst_lst):
    assemble_lst = []
    for src_dict in src_lst:
        for dst_dist in dst_lst:
            assemble_lst.append(dict(src_dict, **dst_dist))
    return assemble_lst


# 将Yaml提供的字典类型转换成列表类型
def yaml_dict2list(dcts):
    return [[key, form_data[key]["values"]] for key in form_data]

# 排列组合
def data_combination(form_data):
    lst = [wrap_lst(item) for item in yaml_dict2list(form_data)]
    res = lst[0]
    if len(lst) == 1:
        return res
    else:
        for i in range(1, len(lst)):
            res = assemble_wrap_lst(res, lst[i])
    return res

if __name__ == "__main__":
    f = open("interface.yml")
    x = yaml.load(f)

    form_data = x["interface"]["body"]
    excep = form_data["except"]
    form_data.pop("except")

    print data_combination(form_data)
