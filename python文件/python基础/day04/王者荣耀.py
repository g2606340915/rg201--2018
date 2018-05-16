haha = [{'name':123,'passwd':321}]

while True:
    print('1、登录','2、注册')
    game = int(input('请输入功能序号'))
    
    def register():    # 注册
        name = input('请输入你要注册的帐号')
        account = []
        for dictionary in haha:
            account.append(dictionary['name'])
        if name in account:
            print('帐号已存在，请重新输入')
        elif name not in account:
            passwd = input('请输入注册密码')
            dic = {}
            dic['name'] = name
            dic['passwd'] = passwd
            haha.append(dic)
            print('注册成功')

    def login():
        name = input('请输入你的帐号')
        for dictionary in haha:
            account = []
            account.append(dictionary['name'])
        if name not in account:
            print('帐号错误，请重新输入')
        elif name in account:
            passwd2 = input('请输入密码')
            i = 0
            lenght = len(haha)
            dic = {}
            while i <= lenght -1:
                dic = haha[i]
                if dic['name'] == name:
                    passwd3 = int(dic['passwd'])
                    print('成功登录游戏')
                    break
                else:
                    i += 1
                    dic = {}
            if passwd2 == passwd3:
                    print('欢迎，你已进入王者荣耀')

    if game == 2:
        register()
    elif game == 1:
        login()
