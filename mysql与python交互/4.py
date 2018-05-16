import pymysql

def connect(ip_addr,user,passwd,db_name):
	
	db = pymysql.connect(ip_addr,user,passwd,db_name,charset=utf8)