import re

# 如果hello的首字符小写，那么正则表达式需要小写的h 
ret = re.match('h', 'hello python')
print(ret.group())
print("*" * 50)

#如果hello的首字符大写，那么正则表达式需要大写的H
ret = re.match('H', 'Hello python')
print(ret.group())
print("*" * 50)

# 大小写h,H都可以的情况
ret = re.match('[hH]', 'hello python')
ret2 = re.match('[hH]', 'Hello python')
print(ret.group())
print(ret2.group())
print("*" * 50)

# 匹配0-9的第一种写法
ret = re.match('[0123456789]', '7hello python')
print(ret.group())
print("*" * 50)

# 匹配0-9的第二种写法
ret = re.match('[0-9]', '7hello python')
print(ret.group())
print("*" * 50)