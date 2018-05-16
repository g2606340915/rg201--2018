# pymysql 是 python 链接MySQL 数据库的模块
import pymysql

# 打开数据库链接
db = pymysql.connect("localhost","root","guobin","mysql")

# 创建一个游标对象
cursor = db.cursor()

# 使用sql语句
cursor.execute('SELECT NOW()')

# 使用fetchone() 方法，获取单条数据
data = cursor.fetchone()

print(data)

# 关闭数据库链接
db.close()

