import re

a = 'ho ver abc'
s = r'.*\bver\b'
result = re.match(s, a).group()
print(result)
print("*" * 50)

a = 'ho verabc'
result = re.match(s, a).group()     # 报错
print("*" * 50)

a = 'hover abc'
result = re.match(s, a).group()     # 报错