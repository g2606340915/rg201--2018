import re

# 正确的地址
ret = re.match('[\w]{4,20}@163\.com', 'zhangsan@163.com').group()
print(ret)

# 不正确的地址
ret = re.match('[\w]{4,20}@163\.com', 'zhangsan@163.comsajhdg').group()
print(ret)

# 通过$符号来确定末尾
ret = re.match('[\w]{4,20}@163\.com$', 'zhangsan@163.comm').group()
print(ret)