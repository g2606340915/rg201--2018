import re

mm = 'c:\\a\\b\\c'
print(mm)
print("*" * 50)
ret = re.match('c:\\\\', mm).group()
print(ret)
print("*" * 50)
ret = re.match('c:\\\\a', mm).group()
print(ret)
print("*" * 50)
# python中字符串前面加上r表示原生字符串
ret = re.match(r'c:\\a', mm).group()
print(ret)