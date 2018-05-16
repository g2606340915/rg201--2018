# 先让用户输入要复制的文件名 
old_file_name = input('请输入要复制的文件名')

# 打开要复制的文件
old_file = open(old_file_name,'r')

# rfind返回的是下标

new_file_name = '[复件]'+old_file_name

# 新建一个文件
new_file = open('lao_wang.txt','w')

# 从旧文件中读取数据，并且写入新的文件中
content = old_file.read()

new_file.write(content)

# 这里是关闭来嗯个打开的文件
old_file.close()
new_file.close()



