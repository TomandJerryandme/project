import requests
# 图片地址
# https://pic1.zhimg.com/v2-533a65954c5ad92d38590da407bde01e_1440w.jpg?source=172ae18b
# 视频地址
# https://haokan.baidu.com/v?pd=wisenatural&vid=1008580542103423667
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                                    " (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
            "Connection": "keep-alive"}
# url = r'https://haokan.baidu.com/v?pd=wisenatural&vid=1008580542103423667'
# r = requests.get(url, headers=header, timeout=15)
# with open(r"D:\back\test_video.mp4", "wb") as f:
#     f.write(r.content)
# f.close()


# bili_url = 'https://www.bilibili.com'
# result = requests.get(bili_url)
# print(result.status_code)
# print(result.content.decode(encoding='utf-8'))