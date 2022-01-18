debug_file_url = r'D:\Visual_Studio_Code\project\Project\Python\debug.txt'
shell_file_url = r'D:\Visual_Studio_Code\project\Project\Python\shell.txt'

debug_model_list = []
shell_model_list = []

with open(debug_file_url, 'r', encoding='utf-8') as file:
    for line in file.readlines():
        debug_model_list = line.split("', '")

with open(shell_file_url, 'r', encoding='utf-8') as file:
    for line in file.readlines():
        shell_model_list = line.split("', '")

for model in shell_model_list:
    if model not in debug_model_list:
        print(model)

for model in debug_model_list:
    if model not in shell_model_list:
        print(model)