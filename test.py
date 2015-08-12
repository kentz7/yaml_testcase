#encoding:utf-8
import yaml
import re

# yml_file_path = "response/user_login.yml"
# yml_file = open(yml_file_path)
# yml_dict = yaml.load(yml_file)
# print yml_dict["key_e10adc3949ba59abbe56e057f20f883e_phone_None"]
# print yml_dict["key_e10adc3949ba59abbe56e057f20f883e_phone_!@#$ASDF"]


# params = ${param1}
# params = ${param1}${param2}
# params = ${param1}${interface aaa bbb}
# test_str = "params = ${param1}/${interface aaa bbb ccc}${interface 111 222 333}"


# reg_str = r"\$\{(\w+)\}"
# reg_str = "\$\{(((\w+\s+)+)(\w+))\}"

# pattern = re.compile(reg_str)
# match = pattern.search(test_str)
#
# if match:
#     print match.group()

# find = re.findall(reg_str, test_str)
# print find


def funcA():
    print "Func A"

def funcB():
    print "Func B"

def funcC():
    print "Func C"



func_dict = {
    "funcA": funcA
}


func_dict["funcA"]()
