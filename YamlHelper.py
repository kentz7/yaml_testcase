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


# 比较两个字典，以src_dict为准
def left_cmp_dict(src_dict, dst_dict):
    for key in src_dict:
        # 递归比较
        if type(src_dict[key]) is dict:
            flag = left_cmp_dict(src_dict[key], dst_dict[key])
            if not flag:
                return False
        else:
            # 如果右侧的字典没有key，则返回False
            if not dst_dict.has_key(key):
                print "右侧字典没有key: {0}".format(key)
                return False
            if not src_dict[key] == dst_dict[key]:
                print "字典值不一致"
                print "src_dict[{0}]: {1}".format(key, src_dict[key])
                print "dst_dict[{0}]: {1}".format(key, dst_dict[key])
                return False
    return True
