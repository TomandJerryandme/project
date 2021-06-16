# 0-侽
# 1-侾
# 2-俀
# 3-俁
# 4-係
# 5-俆
# 6-俇
# 7-俈
# 8-俉
# 9-俋

# 789

KEY_VALUE_DICT = {
    "0": "侽",
    "1":"侾",
    "2":"俀",
    "3":"俁",
    "4":"係",
    "5":"俆",
    "6":"俇",
    "7":"俈",
    "8":"俉",
    "9":"俋",
}

def tran_str(source_obj):
    print_str_list = []
    if isinstance(source_obj, int):
        for i in str(source_obj):
            print_str_list.append(KEY_VALUE_DICT.get(i))
    elif isinstance(source_obj, str):
        for i in source_obj:
            print_str_list.append(list(KEY_VALUE_DICT.keys())[list(KEY_VALUE_DICT.values()).index(i)])
    else:
        print("请输入正确的源数字或者字符")
    print("".join([i for i in print_str_list]))

source_obj = input("请输入源数字：")
if source_obj.isdigit():
    source_obj = int(source_obj)
tran_str(source_obj)