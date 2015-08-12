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
                    YamlHelper.var_expr(variables, expr_line.strip())
                else:
                    self.add_var(variables, expr_line)
