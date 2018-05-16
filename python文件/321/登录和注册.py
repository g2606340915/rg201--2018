def register(account,passwd):
    f = open('account.txt'.'r')
    account_list = f.readlines()
    f.close()
    lenght = len(accounr_list)
    
    if lenght == 0:
        print('这里可以创建帐号')
        f = open('account.txt','w')
        f.write(account)
        f.close
    else:
        names = []
        print('本地有的帐号是：',account_list)
        for name in account_list:
            names.append(name.rstrip())
        if account in names:
            print('帐号已经存在')
        else:
            print('这里可以创建帐号')
            f = open('account.txt','w')
            f.write(account)
            f.close
            
a = input('请输入帐号')
register(a,1)

