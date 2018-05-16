import re

#匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无
ret = re.match('[A-Z][a-z]*', 'Mm')
print(ret.group())
print("*" * 50)
ret = re.match('[A-Z][a-z]*', 'Aaksjdhiuwkj')
print(ret.group())