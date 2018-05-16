# ATM机取款
"""
帐号：123456789
密码：654321
姓名：郭斌
原有的金额：2000
本次要取的金额：500
取完以后剩下的金额：2000-500=1500
"""
id = input("请输入帐号")
password = input("请输入密码")
name = input("请输入您的姓名")
money = input("请输入本次要取金额")

print("帐号:%s\n密码******\n姓名:%s\n本次要取金额:%s\n原有金额:%s"%(id,name,money,2000))

money2 = 2000
difference = money2-int(money)

print("还剩:"+str(difference))
