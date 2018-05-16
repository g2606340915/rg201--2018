import re

a = 'hoverabc'
s = r'.*\Bver\B'
result = re.match(s, a).group()
print(result)
print("*" * 50)

a = 'hover abc'
result = re.match(s, a).group()     # 报错
print(result)
print("*" * 50)

a = 'ho ver abc'
result = re.match(s, a).group()     # 报错
print(result)
print("*" * 50)