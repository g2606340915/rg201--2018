import re

# 匹配以baidu开头的语句
result = re.match('baidu', 'baidu.com')
print(result.group())