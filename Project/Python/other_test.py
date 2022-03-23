import base64

debug_file_url = r'D:\Visual_Studio_Code\project\Project\Python\python_knowledge.txt'
with open(debug_file_url, 'rb') as file:
    x = base64.b64encode(file.read())
    print(x)

# shell_file_url = r'D:\Visual_Studio_Code\project\Project\Python\modify_create.sql'

# debug_model_list = []
# shell_model_list = []

# write_file = open(shell_file_url, 'w', encoding='utf-8')

# str = 'select column_type from information_schame.columns where table_name = %s and column_name = %s'

# def get_column_type(list, str):
#     x = list
#     x.reverse()
#     for sql in x:
#         sss = sql.strip()
#         column_name = str[str.index('.')+1:]
#         if sss.startswith(column_name):
#             list_str = filter(lambda x: x != '', sss.split(' '))
#             xxxxx = []
#             for x in list_str:
#                 xxxxx.append(x)
#             if column_name == xxxxx[0]:
#                 return xxxxx[1]



# path_list = []
# with open(debug_file_url, 'r', encoding='utf-8') as file:
#     for line in file.readlines():
#         line_str = line
#         path_list.append(line_str)
#         if line.startswith('comment on table'):
#             table_name = line[17: line.index(' ', 18)]
#             line_str = 'alter table %s comment\n' % (table_name)
#         if line.startswith('comment on column'):
#             opeate_name = line[18: line.index(' ', 19)]
#             print(opeate_name)
#             table_name = opeate_name[:opeate_name.index('.')]
#             column_name = opeate_name[opeate_name.index('.')+1:]
#             line_str = 'alter table %s modify %s %s comment\n' % (table_name, column_name, get_column_type(path_list, opeate_name))
#         write_file.write(line_str)
# write_file.close()




# # with open(shell_file_url, 'r', encoding='utf-8') as file:
# #     for line in file.readlines():
# #         shell_model_list = line.split("', '")

# # for model in shell_model_list:
# #     if model not in debug_model_list:
# #         print(model)

# for model in debug_model_list:
#     if model not in shell_model_list:
#         print(model)