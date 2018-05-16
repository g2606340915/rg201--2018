# 获取用户要拷贝的文件名
old_file_name = input('请输入要拷贝的文件名：')
old_file = open(old_file_name,'r')

if old_file:
    file_flag_num = old_file_name.find('.')
    if file_flag_num >0:
        file_flag = old_file_name[file_flag_num:]
    new_file_name = old_file_name[:file_flag_num] + '[复件]'+file_flag
    new_file = open(new_file_name,'w')

    for line_content in old_file.readlines():
        new_file.write(line_content)
    old_file.close()
    new_file.close()






