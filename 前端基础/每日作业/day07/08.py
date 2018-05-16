import re 

# 匹配出,8到20位的密码，可以使大小写字母、数字、下划线
ret = re.match('[a-zA-Z0-9_]{6}', '12a3g456787')
print(ret.group())
print("*" * 50)
ret = re.match('[a-zA-Z0-9_]{8,20}', 'dfdfdffga65423187983121as12asdwd564we48').group()
print(ret)
print("*" * 50)