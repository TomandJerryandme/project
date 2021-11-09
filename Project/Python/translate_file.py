# 转换

import sys
import os
from time_counter import _round
# from common.tools import log
# from common.tools.exception import ValidationError
# _logger = log.get_log(__name__)
PATH = os.path
def get_file_size_byte(file_path):
    if not file_path:
        return 0
        # _logger.warning("不存在路径参数, 请重新输入")
        # raise ValidationError("不存在路径参数, 请重新输入")
    file_size  = PATH.getsize(file_path)
    return file_size

def get_target_size(file_path):
    if not file_path:
        # 在最开始调用就校验路径
        return '请输入路径'
    file_size = 0
    if PATH.isfile(file_path):
        # 不是是文件夹， 调用方法 直接计算文件大小
        file_size += get_file_size_byte(file_path)
    elif PATH.isdir(file_path):
        # 是文件夹 需要遍历文件获取数据
        for root, dirs, files in os.walk(file_path):
            file_size += sum([get_file_size_byte(root + '\\' + name) for name in files])
    print(get_format_size(file_size, 'gb', 4))

def get_format_size(file_size, type='MB', digit=3):
    size_kb = _round(file_size/(2**10), digit)
    size_mb = _round(file_size/(2**20), digit)
    size_gb = _round(file_size/(2**30), digit)
    return_dict = {'KB': str(size_kb) + 'KB', 'MB': str(size_mb) + ' MB', 'GB': str(size_gb) + ' GB'}
    return return_dict.get(type.upper())

file_path = 'D:\\qqMessage\\1728703711\\FileRecv\\db0721_2021-10-25_13-05-00'
get_target_size(file_path)



"""
    # 预置数据 重新修改 -- 银行
    file = open("C:\\Users\\liuxuan02\\Desktop\\bank.txt", 'r+', encoding='UTF-8')
    write_file = open("C:\\Users\\liuxuan02\\Desktop\\bank_bak.txt", 'a+', encoding='UTF-8')
    x = file.readlines()
    str = ''
    for line in x:
        if line.startswith('    <!-- '):
            # 找到中文
            start_index = line.index('<!-- ')
            end_index = line.index(' -->')
            str = line[start_index+5:end_index]
        if line.startswith('      <field name="name">'):
            replace_str = '      <field name="name">' + str + '</field>\n'
            write_file.write(replace_str)
            print(replace_str)
        else:
            write_file.write(line)
            print(line)
"""
'''
    # 中文转换编码
    while(True):
        source_str = input("请输入原中文: ")
        if source_str == 'exit':
            break
        print(source_str.encode('unicode-escape').decode())
    sys.exit()
'''