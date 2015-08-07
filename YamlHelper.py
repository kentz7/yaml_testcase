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


# 获取两个字符串相同的前缀
def same_prefix(pre_string, post_string):
    min_len = len(pre_string) if len(pre_string) < len(post_string) else len(post_string)
    flag = 0
    for i in range(min_len):
        if pre_string[i] == post_string[i]:
            flag = i
            continue
        else:
            break
    if flag == 0:
        return None
    return pre_string[0:flag+1]
