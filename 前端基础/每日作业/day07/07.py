import re

# 匹配出0到99之间的数字
ret = re.match('[1-9]?[0-99]', '7')
print(ret.group())

ret = re.match('[1-9]?[0-9]', '33')
print(ret.group())

ret = re.match('[1-9]?[0-9]', '09')
print(ret.group())