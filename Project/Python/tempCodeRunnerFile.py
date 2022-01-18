import requests 

# data = {
#     "model": "pur.order"
# }
data = {
    "modelId": "pur.order",
    "dataId": "5"
}
header = {
    "Content-type": "application/json",
    "Cookie": "Hm_cv_c9586ee23a98cd8f76bb7f934e6e8d9a=*!*!*!1*User Access Level*Normal User; session_id=1a39159167dd38c55a8ca47792b088d957f49681; caf_web_session=N2EwMjk4OWEtYzEyZC00MGQ4LWJiMTUtMmI1Njk4MTYzMDRl; Hm_lvt_c9586ee23a98cd8f76bb7f934e6e8d9a=1640678983,1640742788,1640915616,1641349821; Hm_lpvt_c9586ee23a98cd8f76bb7f934e6e8d9a=1641456015",
}
# url = 'https://igix.insuite.net/api/runtime/insuite/v1.0/be/sync'
url = 'https://igix.insuite.net/api/runtime/wf/v1.0/procDefs/modelId'
result = requests.post(url=url, json=data, headers=header)
print(result.status_code)
print(result.text)