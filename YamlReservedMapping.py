#encoding: utf-8

def interface(yaml_file_name, **args):
    # ${interface yaml_file_name param1 param2 param3}
    # 先获取到该yaml文件

    # 直接调用single_request方法
    
    return "1234567890"


def interface1(param):
    print "interface 11111"
    return "1234567890"


def interface2(param):
    print "interface 22222"
    return "0123456789"


ReservedMapping = {
    "interface": interface,
    "interface1": interface1,
    "interface2": interface2
}
