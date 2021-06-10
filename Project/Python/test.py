import random
from itertools import combinations,permutations
from datetime import datetime

# len = 86
test_word = ['0','1','2','3','4','5','6','7','8','9',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        '!','@','#','$','%','^','&','*','(',')','-','_','=','+','/','~','`','<','>','?',',','.',';',':']

len = eval(input("请输入长度："))
old_password = "adk"
old_list = random.sample(test_word, len)
# print(old_list)
# for i in old_list:
#     old_password += i
# print(old_password)

begin_time = datetime.now()
back_list = permutations(test_word, len)
# print(str(len(back_list)))
for test in back_list:
    new_password = ""
    for x in test:
        new_password += x
    if new_password == old_password:
        print("old=%s, new=%s" % (old_password, new_password))
        time = datetime.now() - begin_time
        print(str(time))
        break