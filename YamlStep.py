#encoding:utf-8
import YamlHelper

class YamlStep():
    # 构造函数
    def __init__(self, expr_lines):
        self.expr_lines = expr_lines

    # 处理变量
    def add_var(self, variables, variable_line):
        variable_name = variable_line.split("=")[0].strip()
        variables[variable_name] = YamlHelper.var_expr(variables, variable_line.split("=")[1].strip())


    # 执行操作
    def execute(self, variables):
        # 如果没有设置前置或后置则无需执行
        if self.expr_lines:
            for expr_line in self.expr_lines:
                if "=" not in expr_line:
                    print YamlHelper.var_expr(variables, expr_line.strip())
                else:
                    self.add_var(variables, expr_line)


if __name__ == "__main__":
    variables = {'Username': 'kentz', 
    'A': 'TEST AAAAAA', 
    'B': 'TEST AAAAAA/password', 
    'Version': 'v2', 
    'param3': 'TEST AAAAAA/0123456789/asjdlkfjalk', 
    'param2': 'TEST AAAAAA/0123456789', 
    'param1': '1234567890', 
    'Password': '123456'}
# - user/login/${SessionID}
# - user/login/${GetSession kentz}
# - user/login/${SessionID}/${Func param}
# - user/login/
    pre = YamlStep(["/user/login/${single_execute user_login kentz phone e10adc3949ba59abbe56e057f20f883e}"])
    pre.execute(variables)