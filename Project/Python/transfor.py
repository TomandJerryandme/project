import os
import sys
import logging

_logger = logging.getLogger(__name__)

# -*- coding: utf-8 -*-
# 该文件主要用于各种转换
# 1、进制之间的转换
# 2、大小写的转换
# 3、

DECIMAL_DICT = {
    2: bin,
    8: oct,
    10: int,
    16: hex,
}

def decimal_transfor(old_value, old_decimal, new_decimal):
    """
        desc:   进制转换：通过传入原来进制与值，并指定要转换的进制，获得转换后的进制的值
        params: old_decimal 原进制
                new_decimal 新进制
        return: 返回值（转换后的进制值）
        # 下面函数的参数都是十进制数字
            # 二进制    bin()
            # 八进制    oct()
            # 十六进制  hex()
        # int()方法可以将数字形式字符串转换为对应进制的数字，并最终转换为10进制
        # 十进制    int()
    """
    new_func = DECIMAL_DICT.get(int(new_decimal))
    # 这种用法只能在int方法上使用，其他三个函数都只有一个形参
    value = int(old_value, int(old_decimal))
    return new_func(int(value))


def upper_and_lower_transfor(origin_str, type="", is_head_lower=False, is_body_change=False):
    """
        desc: 进行字符串大小写的转换
            有多种转换形式（全部转换-all、转换首字母-head、转换首字母后其他转另外一种-body）
        params: origin_str  原字符串
                type 转换形式（全部转换、转换首字母）, 默认为全部转换
                is_head_lower 首字母是否转为小写
                is_body_change 非首字母是否转换
    """
    if type == 'all':
        if is_head_lower:
            return origin_str.lower()
        else:
            return origin_str.upper()
    elif is_body_change:
        return_str = ''
        if is_head_lower:
            return_str.append(origin_str[0].lower())
            return_str.append(origin_str[1:].upper())
        else:
            return_str.append(origin_str[0].upper())
            return_str.append(origin_str[1:].lower())
        return "".join(return_str)
    else:
        other_str = origin_str[1:]
        return "".join(origin_str[0].lower() + other_str if is_head_lower else origin_str[0].upper() + other_str)



if __name__ == "__main__":
    # 通过命令行传过来参数(注意，命令行调用python在该文件中只能使用相对路径,如果要使用绝对路径，需要将文件名使用字符串类型传入，不能直接在命令行中使用，因为存在空格)
    # 可以通过 python 的命令解析模块 optparse 来进行
    # 通过sys.argv[]获取参数
    # 在sys.argv中，是由python3/python来作为开始的
    # eg: python3 test_main.py -c config.conf -d 12.2       其中sys.argv是在test_main.py中调用的
    # 则在这一个指令中，参数列表为： ['test_main.py', '-c', 'config.conf', '-d', '12.2']
    # eg2: python3 -d test_main.py -c config.conf -d 12.2
    # 在该指令中，参数列表为： ['test_main.py', '-c', 'config.conf', '-d', '12.2']
    # 并不会在 test_main.py 前 有个 -d 的参数
    # print(sys.argv)
    # print(os.path.dirname(__file__))    # d:\Visual Studio Code\project\Project\Python
    # eg:
    #   python "D:\Visual Studio Code\project\Project\Python\transfor.py" -dec 1010 2 16 -str abCdef body True False
    result = ""
    sys.argv = sys.argv[1:]
    if "-dec" in sys.argv:
        index = sys.argv.index("-dec")
        value = sys.argv[index+1]
        old_decimal = sys.argv[index+2]
        new_decimal = sys.argv[index+3]
        dec_result = decimal_transfor(value, old_decimal, new_decimal)
        result = result + "\n" + str(dec_result)
    if "-str" in sys.argv:
        str_index = sys.argv.index("-str")
        origin_str = sys.argv[str_index+1]
        type = sys.argv[str_index+2]
        is_head_lower = eval(sys.argv[str_index+3])
        is_body_change = eval(sys.argv[str_index+4])
        str_result = upper_and_lower_transfor(origin_str=origin_str, type=type, is_head_lower=is_head_lower, is_body_change=is_body_change)
        result = result + "\n" + str(str_result)

    print(result)
    