#encoding:utf-8

import YamlDefault

# 根据参数类型获取默认值
def yaml_default(value_type):
    if value_type == "string":
        return YamlDefault.VARIABLE_STRING
    elif value_type == "int":
        return YamlDefault.VARIABLE_INT
    elif value_type == "bool":
        return YamlDefault.VARIABLE_BOOL
    else:
        return None


# 根据key来获取值，如果key不存在，则使用默认值
def http_option(dct, key):
    if dct.has_key(key):
        return dct[key]
    else:
        return YamlDefault.HTTP_DEFAULT[key]
