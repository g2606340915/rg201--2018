account_list = []
def login(account='李白',passwd='123456'):
    for dic in account_list:
        if account == dic['name']:
            if dic['passwd'] == passwd:
                print('登录成功')
            else:
                print('密码错误')
        else:
            print('帐号输入错误')

account = input('请输入帐号')
passwd = input('请输入密码')   
login(account,passwd) 
