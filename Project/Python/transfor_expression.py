# -*- coding: utf-8 -*-

# 前缀、中缀、后缀表达式之间的相互转换

class TransforExpress():
    def __init__(self, origin_express):
        # 该方法的作用，判断出原表达式是那种类型并记录下来
        self.type = 0
        self.origin_express = origin_express
    
    def transfor_express(self, target_type):
        """
            @desc: 将原本的表达式转换为target_type类型的表达式
            @params:
                target_type: 目标类型
            @return
                目标情况(str)
        """