import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
# 收件人
mail.To = 'liuxuan02@inspur.com'
# 抄送人
# mail.CC = 'wanglijuan01@inspur.com; niyulu@inspur.com'
# 邮件主题
mail.Subject = '邮件主题内容'
# 邮件正文
message = """
抱歉，两位大佬，运行错代码了，尴尬
"""
# 获取签名，必须在对邮件正文赋值之前进行获取，获取后，签名存放在 mail.HTMLBody 里面
mail.GetInspector
# 将签名与正文放在一起，签名要放在后面
mail.HTMLBody = message + mail.HTMLBody
mail.BodyFormat = 2
# 设置重要性为高
mail.Importance = 2
# 调用Outlook显示
mail.Display()
# 发送
mail.Send()