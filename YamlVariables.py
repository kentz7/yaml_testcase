#encoding:utf-8
import re
import YamlHelper
import YamlReservedMapping

class YamlVariables():
    # 构造函数
    def __init__(self, variable_lines):
        self.variables = {}

        for variable_line in variable_lines:
            # 如果有变量名，则保存 => 就是有 = 符号
            if "=" not in variable_line:
                # 这样也貌似没有任何意义
                print "全局变量定义中，存在没有赋值的用法: {0}".format(variable_line)
            else:
                # 如果没有变量名，则只执行
                self.add_var(variable_line)


    # 处理变量
    def add_var(self, variable_line):
        variable_name = variable_line.split("=")[0].strip()
        # self.variables[variable_name] = self.expr(variable_line.split("=")[1].strip())
        self.variables[variable_name] = YamlHelper.var_expr(self.variables, variable_line.split("=")[1].strip())


    # 返回变量值
    def get(self, var_name):
        if self.variables.has_key(var_name):
            return self.variables[var_name]
        print "不存在全局变量: {0}".format(var_name)
        return None
