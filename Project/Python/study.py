# 刷网课
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
urls = [
    # 课件地址列表
]

client = webdriver.Chrome()

def login(user, pwd):
    # 模拟登录操作
    login_btn = WebDriverWait(client, 10, 0.5).until(EC.presence_of_element_located((By.ID, "btnLogin2")))
    # 在找到的element里面键入 user，pwd信息
    client.find_element(By.NAME, "txtUserName2").send_keys(user)
    client.find_element(By.NAME, "txtPassword2").send_keys(pwd)
    # 点击校验
    client.find_element(By.ID, "chkloginpass").click()
    # 点击登录按钮
    login_btn.click()


def study_lesson():
    try:
        v = WebDriverWait(client, 5, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//video[@id="vjs_video_3_html5_api"]')))
        v.click()
    except Exception as e:
        pass
    p = client.find_elements(By.XPATH, r'//input[@value="继续学习"]')
    if p:
        p[0].click()
    while True:
        try:
            client.execute_script("if ($('#vjs_video_3_html5_api')[0].paused){$('#vjs_video_3_html5_api')[0].play();}")
        except Exception as e:
            pass
        restart_study = client.find_elements(By.ID, "reStartStudy")
        if restart_study:
            restart_study[0].click()
        elif client.find_elements(By.XPATH, r'//span[@id="ScheduleText"][text()="100%"]'):
            # 监控学习进度，如果达到100%，立即停止，进行下一项任务
            break
        # 进行每秒一次的轮询
        time.sleep(1)


def main():
    # chrome 浏览器最大化操作  minimize_window 最小化
    # forword 前进，  back 回退
    client.minimize_window()
    # client.get(url="登录网址")
    # login(登录名, 登录密码)
    WebDriverWait(client, 10, 0.5).until(
        EC.presence_of_element_located((By.XPATH, r'//a[@id="hylIndex0"][text()="我的学习"]')))
    for url in urls:
        # 打开学习地址
        client.execute_script('window.open("{}")'.format(url))
        client.close()
        client.switch_to.window(client.window_handles[-1])
        study_lesson()


if __name__ == '__main__':
    main()