#encoding:utf-8
import re
import YamlDefault
import YamlReservedMapping

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


# 根据key来获取值
def yaml_tag_value(dct, key):
    # 先判断dct有没有该key
    if dct.has_key(key):
        return dct[key]
    # 如果dct没有，再看default_values中是否有该key
    elif YamlDefault.DEFAULT_VALUES.has_key(key):
        return YamlDefault.DEFAULT_VALUES[key]
    # 都没有就返回None
    else:
        return None


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
                print u"右侧字典没有key: {0}".format(key)
                return False
            if not src_dict[key] == dst_dict[key]:
                print "字典值不一致"
                print "src_dict[{0}]: {1}".format(key, src_dict[key])
                print "dst_dict[{0}]: {1}".format(key, dst_dict[key])
                return False
    return True


# 调用预定义函数
def invoke_reserved(func_line):
    # func_line格式: func_name param1 param2 param3
    func_name = func_line.split(" ")[0]
    param_list = ",".join(func_line.split(" ")[1:])
    return YamlReservedMapping.ReservedMapping[func_name](param_list)


# 字符串中替换 已定义变量 和 预定义函数
def var_expr(variables, expr_line):
    # 先判断是否有引用变量，引用变量正则: ${\w+}  /  ${(\w+\s+)+\w+}
    # 如果有引用，则替换该变量（有可能有多个引用）
    # 引用分两种情况:(可能同时存在变量和方法调用)
    # 1. 引用已定义的变量
    result = expr_line
    reg_var = r"\$\{(\w+)\}"
    find_var_lst = re.findall(reg_var, expr_line)
    if len(find_var_lst):
        for var_name in find_var_lst:
            if not variables.has_key(var_name):
                print u"不存在全局变量: {0}".format(var_name)
                return
            # 替换字符串
            result = result.replace("${" + var_name + "}", variables[var_name])

    # 2. 调用预定义方法
    # 返回一个元组列表, 如: [('interface aaa bbb ccc', 'interface aaa bbb ', 'bbb ', 'ccc')]
    reg_func = r"\$\{(((\w+\s+)+)(\w+))\}"
    find_func_lst = re.findall(reg_func, expr_line)
    if len(find_func_lst):
        for func_line in find_func_lst:
            result = result.replace("${" + func_line[0] + "}", invoke_reserved(func_line[0]))

    # 3. 没有任何引用则直接赋值
    print u"{0} 全局变量/预定义函数调用后的表达式: {1}".format(expr_line, result)
    return result


# 只支持一维的字典（不支持复合字典）
def dict_var_expr(variables, dct):
    for dct_key in dct:
        dct[dct_key] = var_expr(variables, dct[dct_key])
    return dct
