#encoding: utf-8
from YamlInterface import YamlInterface
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

def single_execute(param):
    param_dst = {}
    key_lst = []
    param_lst = param.split(',')
    interface = YamlInterface("interface/" + param_lst[0] + ".yml")
    sorted_key_item = sorted(interface.body.iteritems(), key=lambda k:k[0], reverse=False)
    i = 1
    for item in sorted_key_item:
        # key_lst.append(item[0])
        param_dst[item[0]] = param_lst[i]
        i = i + 1 
    print param_dst
    response_text = interface.single_request(**param_dst)
    print response_text
    return "fsfgsd"

ReservedMapping = {
    "interface": interface,
    "interface1": interface1,
    "interface2": interface2,
    "single_execute": single_execute
}
