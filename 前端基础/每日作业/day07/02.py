import re 

# 匹配任意一个字符
ret = re.match('.', 'a')
print(ret.group())

ret = re.match('.', 'b')
print(ret.group())

ret = re.match('.', 'M')
print(ret.group())