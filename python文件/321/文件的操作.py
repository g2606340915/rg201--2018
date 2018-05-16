# open()

# write()
# read()
# close()
# w写 r读
# 如果 有这个文件就打开，没有这个文件就创建


'''
f = open('guobin','w')
f.write('哈哈哈')
f.close
'''


# 注册
def register(account,password):
    # 创建一个用于存储帐号的文件
    f = open('account.txt','w+')
    f.write(account)
    f.close()
    f2 = open('password.txt','w+')
    f2.write(password)
    f2.close()

# 登录
def login(account,password):
    f = open('account.txt','r')
    b = f.readlines()
    f2 = open('password.txt','r')
    b2 = f2.readlines()   
    if a == account:
        if b == password:
            print('登录成功')
    else:
        print('帐号不存在')
    # f.close()
    # f2.close()

# 删除

def shan_chu(account,password):
    f = open('account.txt','w+')
    b = f.readlines()
    f2 = open('password.txt','w+')
    b2 = f2.readlines()
    count=0
    for a in b:
        if a == account:
            del b[count]
            del b2[count]
            count+=1
        else:
            print('请输入正确的帐号和密码')
a = input('输入帐号')
b = input('输入密码')
# register(a,b)
# login(a,b)
shan_chu(a,b)
