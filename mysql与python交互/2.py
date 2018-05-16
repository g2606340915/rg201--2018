import pymysql

# 链接数据库
db = pymysql.connect('localhost','root','guobin','mysql',charset='utf8')

# 创建游标对象
cursor = db.cursor()

# # 执行sql语句
# sql = '''create table students2(id int auto_increment primary key,name varchar(20) )'''
# cursor.execute(sql)

sql = "insert into students2 values(0,'zhang')"
try:
	cursor.execute(sql)

	db.commit()
except Exception as e:
	print('报错')
	db.rollback()

# 关闭数据库
db.close()