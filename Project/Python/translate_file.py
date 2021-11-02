# 转换

import sys

"""
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

# 中文转换编码
while(True):
    source_str = input("请输入原中文: ")
    if source_str == 'exit':
        break
    print(source_str.encode('unicode-escape').decode())
sys.exit()