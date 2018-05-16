import pymysql

# 链接数据库
db = pymysql.connect('localhost','root','guobin','mysql',charset='utf8')

# 创建一个游标对象
cursor =db.cursor()

# 这就是一个简单的SQL
sql='select * from students2 where age >= 50'

try:
	# 语句正常执行sql语句
	print('正常')

	# 让游标对象去执行sql语句
	cursor.execute(sql)

	# 我把结果集放到一个变量a里面
	a = cursor.fetchall()
	print(a)

	# 提交事物
	db.commit()
	
except Exception as e:
	print(e)
	db.rollback()

db.close()