import easygui as g
msg = """
[*真实姓名]为必填项
[*手机号码]为必填项
[*E-mail]为必填项
"""
title = "账号中心"
(user_id, name, phone,cellphone, qq, email) = g.multenterbox(msg, title, ["*用户名", "*真实姓名", "固定电话", "*手机号码", "QQ", "*E_mail"])
