# python中logging的用法

import logging

# _logging = logging.getLogger(__name__)
# print(_logging.disabled)
# # _logging.info("info")
# _logging.warn("warn")
# _logging.warning("warning")
# _logging.debug("debug")
# _logging.error("error")

str_code = '发射๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊'
# len(str_code) = 326
# 其中 射上面的那些字符是MBCS字符编码，
print(str_code[3].encode('utf-8'))
# b'\xe0\xb9\x8a'   utf-8对应编码