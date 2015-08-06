#encoding:utf-8

import YamlDefault

def yaml_default(value_type):
    if value_type == "string":
        return YamlDefault.VARIABLE_STRING
    elif value_type == "int":
        return YamlDefault.VARIABLE_INT
    elif value_type == "bool":
        return YamlDefault.VARIABLE_BOOL
    else:
        return None
