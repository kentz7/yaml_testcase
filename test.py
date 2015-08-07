#encoding:utf-8
import yaml

yml_file_path = "response/user_login.yml"
yml_file = open(yml_file_path)
yml_dict = yaml.load(yml_file)
#print yml_dict["key_e10adc3949ba59abbe56e057f20f883e_phone_None"]
#print yml_dict["key_e10adc3949ba59abbe56e057f20f883e_phone_!@#$ASDF"]


#
dct = {'domain': 'user', 'code': 0, 'data': {'uuid': '02148450-33be-11e5-a724-c37b4040a649', 'mobile': None, 'picture_url': '', 'register_time': 1437932687637, 'identify_type': 'weixin', 'sex': 'female', 'birthday': None, 'role': 'customer', 'unid': 1000000002165, 'address': None, 'nickname': '', 'email': None, 'identify_id': ''}, 'message': 'Success'}

for item in  dct.iteritems():
    print item
