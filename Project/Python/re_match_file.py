# -*- coding: utf-8 -*-
import re
"""
\w	            匹配数字字母下划线           '[A-Za-z0-9_]'
\W	            匹配非数字字母下划线          '[^A-Za-z0-9_]'
\s	            匹配任意空白字符             '[\t\n\r\f]'
\S	            匹配任意非空字符              '[^\f\n\r\t\v]'
\d	            匹配任意数字                  '[0-9]'
\D	            匹配任意非数字                 '[^0-9]'
\A	            匹配字符串开始
\Z	            匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
\z	            匹配字符串结束
\G	            匹配最后匹配完成的位置。
\b	            匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B	            匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等。	    匹配一个换行符。匹配一个制表符, 等
\1...\9	        匹配第n个分组的内容。
\10	            匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式

[A-Za-z0-9 \-]+       # 只匹配英文、数字、空格、-
[\u4e00-\u9fa5 、\-0-9]+      # 只匹配中文字符、中文顿号、-、数字以及空格
"""



xml_file = open("C:\\Users\\liuxuan02\\Desktop\\source.txt", "r+", encoding="utf-8")
str_value = xml_file.read()

# 匹配英文、数字、空格、-、英文标点、$等
# source_str_pattern = re.compile(r'<field name="name">([A-Za-z0-9$,\. \-]+)</field>')
# source_results = source_str_pattern.findall(str_value)
# for source_result in source_results:
#     print(source_result)

# 以下代码只匹配中文字符、中文顿号、-、数字以及空格
# compile_obj = re.compile(r'<!-- <field name="name">([\u4e00-\u9fa5 、\-0-9]+)</field> -->')
# results = compile_obj.findall(str_value)
# for result in results:
#     print(result)

id_pattern = re.compile(r'id="(\w+)')
id_results = id_pattern.findall(str_value)
# print(type(id_results))
# for result in id_results:
#     print(result)


def get_re_match(source_string, pattern_string):
    pattern = re.compile(pattern_string)
    results = pattern.findall(source_string)
    if len(results):
        return results
    else:
        print('无对应匹配')