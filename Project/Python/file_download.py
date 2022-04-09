import os
import requests
import time

def downloadFile(url,filepath):
    """
    下载任何格式的网络文件
    :param url: 文件的链接地址
    :param filepath: 存放的本地路径包含文件名
    :return: 返回成功状态和耗时(秒)
    """
    if os.path.exists(filepath):
        return "True,0.300"
    else:
        try:
            header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                                    " (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}

            st = int(round(time.time() * 1000))
            r = requests.get(url, headers=header, timeout=15)
            r.raise_for_status()
            with open(filepath, "wb") as f:  # wb：以二进制方式写入文件，如果文件存在会覆盖
                f.write(r.content)  # r.content：以二进制方式读取文件,然后写入
            f.close()
            et = int(round(time.time() * 1000))
            ht = str((et-st)/1000)  # 耗时
            return "True," + ht
        except:
            return "False,0.300"

str = b''
print(str.decode(encoding='utf-8'))