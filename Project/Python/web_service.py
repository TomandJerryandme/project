# 使用python操作web浏览器
# https://translate.google.cn/?sl=zh-CN&tl=en&text=%s&op=translate
# import os

# x = os.popen(["Google Chrome", "https://translate.google.cn/?sl=zh-CN&tl=en&text=翻译&op=translate"])

# print(x.read())


from selenium import webdriver
import urllib3
import urllib
from urllib import request

def mac():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://translate.google.cn/?sl=zh-CN&tl=en&text=翻译&op=translate")


header = ''':authority: translate.google.cn
:method: GET
:path: /?sl=zh-CN&tl=en&op=translate
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: max-age=0
cookie: _ga=GA1.3.1889989754.1596527976; NID=208=UNHTwYE8tjWjLu6IU8a6Z9sk-PUT4559HvCGo5HE6Na3KWdBqCAFrsB_QosREtFNzd59Jt0MNoF2ozhrhTh1ZfgBB85bu8yzODLovtX0COdZrVw_8grWfbrovKwTwKcm-tbpO7pDwXNi4N8QBABPxg3-r6hi0XGMB0VxttsxZq4; OTZ=6012569_24_24__24_; _gid=GA1.3.1855549794.1623395358
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
sec-ch-ua-mobile: ?0
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36
x-client-data: CJS2yQEIpLbJAQjBtskBCKmdygEI1IfLAQjQmssBCKOgywEIwKDLAQjc8ssBCJT1ywEIv/bLAQiz+MsBGI6eywE=
Decoded:
message ClientVariations {
  // Active client experiment variation IDs.
  repeated int32 variation_id = [3300116, 3300132, 3300161, 3313321, 3326932, 3329360, 3330083, 3330112, 3340636, 3340948, 3341119, 3341363];
  // Active client experiment variation IDs that trigger server-side behavior.
  repeated int32 trigger_variation_id = [3329806];
}'''

# req = urllib3.request(url="https://translate.google.cn/?sl=zh-CN&tl=en&text=翻译&op=translate")

# page = req.urlopen("https://translate.google.cn/?sl=zh-CN&tl=en&text=翻译&op=translate")   
# contents = page.read()   
# #获得了整个网页的内容也就是源代码  
# print(contents)


# import requests
# html = requests.get('https://translate.google.cn/?sl=zh-CN&tl=en&text=无耻&op=translate')
# print(html.text)



#!/usr/bin/env python

# -*- coding: utf-8 -*-

_author_ = 'GavinHsueh'

import requests

import bs4

#要抓取的目标页码地址

url = 'http://www.ranzhi.org/book/ranzhi/about-ranzhi-4.html'

#抓取页码内容，返回响应对象

response = requests.get(url)

#查看响应状态码

status_code = response.status_code

#使用BeautifulSoup解析代码,并锁定页码指定标签内容

content = bs4.BeautifulSoup(response.content.decode("utf-8"), "lxml")

element = content.find_all(id='book')

print(status_code)

print(element)
