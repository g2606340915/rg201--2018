import re
# 普通的匹配方式
ret = re.match('天宫1号', '天宫1号发射成功')
print(ret.group())
print("*" * 50)
ret = re.match('天宫2号', '天宫2号发射成功')
print(ret.group())
print("*" * 50)
ret = re.match('天宫3号', '天宫3号发射成功')
print(ret.group())
print("*" * 50)

# 使用\d进行匹配
ret = re.match('天宫\d号', '天宫1号发射成功')
print(ret.group())
print("*" * 25)
ret = re.match('天宫\d号', '天宫2号发射成功')
print(ret.group())
print("*" * 25)
ret = re.match('天宫\d号', '天宫3号发射成功')
print(ret.group())
print("*" * 25)
