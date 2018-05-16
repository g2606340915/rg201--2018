'''

1、登录
2、添加商品
3、节日，商品打折（修改）
4、退出系统
'''

tb_0 = '简约版淘宝莫后控制系统'
print(tb_0.center(20))
print('*'*30)
print('情况1：%s\n情况2：%s\n情况3：%s\n情况4：%s\n'%('登录','添加商品','商品打折','退出系统'))
print('*'*30)
print('')

# 现在，为了保障用户的支付安全，我们需要账号和密码登录
# 使用一个数组（列表）来储存用户输入的账号和密码
# 在这里，我自己先在淘宝APP上定义一个默认的帐号和密码

# 帐号一
name1 = 2606340915
mi_ma1 = 2606340915

# 帐号二
# name2 = 647722485
# mi_ma2 = 647722485

# 登录(login)
account = int(input('请输入帐号'))
passwd = int(input('请输入密码'))

# 使用箭头来表示流程
jian_tou = ('*'*3)
print(jian_tou.center(7))
print(jian_tou.center(7))
print(jian_tou.center(7))
print(jian_tou.center(7))
jian_tou1 = ('*'*5)
print(jian_tou1.center(7))
jian_tou2 = ('*'*3)
print(jian_tou2.center(7))
jian_tou3 = ('*')
print(jian_tou3.center(7))


# 这里使用 if 条件来判断帐号和密码是否输入正确
if account == name1 and passwd == mi_ma1:
    print('登录成功')
    print('-'*30)

    # 添加商品(commodity),显示出所有商品
    print('***@幸运者，恭喜你，今天是11.11,在今天你将享受到以下商品的4.5折优惠***')
    print(' **                                                                **')
    print('  *                                                                *')
    
    # 将有优惠的商品进行列表
    commodity = ['飞科剃须刀','耐克运动鞋','iphone x']
    print(commodity)
    
    # 点击商品
    
    buy = input('挑选你要购买的商品名称')
    if buy == commodity[0]:
        print('你要购买的商品是：%s'%commodity[0])

        print('输入1,确定购买。。输入2,确认返回')

        num = int(input('请输入命令数字'))

        if num == 1:
            print('你已经确认购买该商品')

            yuan_jia = 100
            da_zhe = 100*0.45

            print('飞科剃须刀的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
            fu_kuan = int(input('请付款：'))
            if fu_kuan == da_zhe:
                print('付款成功，预计三天后和你见面')
                print('+'*30)
                print('本次服务到此结束')
            elif fu_kuan < da_zhe:
                print('支付金额不够,有钱了再来，将为你自动退出')
                print('+'*30)
                print('本次服务到此结束')
            else:
                print('多谢大爷打赏，您的物件已被标为快件')
                print('+'*30)
                print('本次服务到此结束')

        elif num == 2:
            buy = input('挑选你要购买的商品名称')
            if buy == commodity[1]:
                print('你要购买的商品是：%s'%commodity[1])

                print('输入1,确定购买。。输入2,确认返回')

                num = int(input('请输入命令数字'))

                if num == 1:
                    print('你已经确认购买该商品')

                    yuan_jia = 200
                    da_zhe = 200*0.45

                    print('耐克运动鞋的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
                    fu_kuan = int(input('请付款：'))
                    if fu_kuan == da_zhe:
                        print('付款成功，预计三天后和你见面')
                        print('+'*30)
                        print('本次服务到此结束')
                    elif fu_kuan < da_zhe:
                        print('支付金额不够,有钱了再来，将为你自动退出')
                        print('+'*30)
                        print('本次服务到此结束')
                    else:
                        print('多谢大爷打赏，您的物件已被标为快件')
                        print('+'*30)
                        print('本次服务到此结束')

                elif num == 2:
                    buy = input('挑选你要购买的商品名称')
                    if buy == commodity[2]:
                        print('你要购买的商品是：%s'%commodity[2])

                        print('输入1,确定购买。。输入2,确认返回')

                        num = int(input('请输入命令数字'))

                        if num == 1:
                            print('你已经确认购买该商品')

                            yuan_jia = 3000
                            da_zhe = 3000*0.45

                            print('iphone x 的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
                            fu_kuan = int(input('请付款：'))
                            if fu_kuan == da_zhe:
                                print('付款成功，预计三天后和你见面')
                                print('+'*30)
                                print('本次服务到此结束')
                            elif fu_kuan < da_zhe:
                                print('支付金额不够，有钱了再来，将为你自动退出')
                                print('+'*30)
                                print('本次服务到此结束')
                            else:
                                print('多谢大爷打赏，您的物件已被标为快件')
                                print('+'*30)
                                print('本次服务到此结束')
                        else:
                            pass
            elif buy == commodity[2]:
                print('你要购买的商品是：%s'%commodity[2])

                print('输入1,确定购买。。输入2,确认返回')

                num = int(input('请输入命令数字'))

                if num == 1:
                    print('你已经确认购买该商品')

                    yuan_jia = 3000
                    da_zhe = 3000*0.45

                    print('iphone x 的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
                    fu_kuan = int(input('请付款：'))
                    if fu_kuan == da_zhe:
                        print('付款成功，预计三天后和你见面')
                        print('+'*30)
                        print('本次服务到此结束')
                    elif fu_kuan < da_zhe:
                        print('支付金额不够，有钱了再来，将为你自动退出')
                        print('+'*30)
                        print('本次服务到此结束')
                    else:
                        print('多谢大爷打赏，您的物件已被标为快件')
                        print('+'*30)
                        print('本次服务到此结束')

                elif num == 2:
                    buy = input('挑选你要购买的商品名称')
                    if buy == commodity[1]:
                        print('你要购买的商品是：%s'%commodity[1])

                        print('输入1,确定购买。。输入2,确认返回')

                        num = int(input('请输入命令数字'))

                        if num == 1:
                            print('你已经确认购买该商品')

                            yuan_jia = 200
                            da_zhe = 200*0.45

                            print('耐克运动鞋的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
                            fu_kuan = int(input('请付款：'))
                            if fu_kuan == da_zhe:
                                print('付款成功，预计三天后和你见面')
                                print('+'*30)
                                print('本次服务到此结束')
                            elif fu_kuan < da_zhe:
                                print('支付金额不够，有钱了再来，将为你自动退出')
                                print('+'*30)
                                print('本次服务到此结束')
                            else:
                                print('多谢大爷打赏，您的物件已被标为快件')
                                print('+'*30)
                                print('本次服务到此结束')
                        else:
                            pass
    elif buy == commodity[1]:
       
        print('你要购买的商品是：%s'%commodity[1])

        print('输入1,确定购买。。输入2,确认返回')

        num = int(input('请输入命令数字'))

        if num == 1:
            print('你已经确认购买该商品')

            yuan_jia = 200
            da_zhe = 200*0.45

            print('耐克运动鞋的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
            fu_kuan = int(input('请付款：'))
            if fu_kuan == da_zhe:
                print('付款成功，预计三天后和你见面')
                print('+'*30)
                print('本次服务到此结束')
            elif fu_kuan < da_zhe:
                print('支付金额不够，有钱了再来，将为你自动退出')
                print('+'*30)
                print('本次服务到此结束')
            else:
                print('多谢大爷打赏，您的物件已被标为快件')
                print('+'*30)
                print('本次服务到此结束')

        elif num == 2:
            buy = input('挑选你要购买的商品名称')
            if buy == commodity[2]:
                print('你要购买的商品是：%s'%commodity[2])

                print('输入1,确定购买。。输入2,确认返回')

                num = int(input('请输入命令数字'))
 
                if num == 1:
                    print('你已经确认购买该商品')
    
                    yuan_jia = 300
                    da_zhe = 300*0.45
  
                    print('iphone x 的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
                    fu_kuan = int(input('请付款：'))
                    if fu_kuan == da_zhe:
                        print('付款成功，预计三天后和你见面')
                        print('+'*30)
                        print('本次服务到此结束')
                    elif fu_kuan < da_zhe:
                        print('支付金额不够，有钱了再来，将为你自动退出')
                        print('+'*30)
                        print('本次服务到此结束')
                    else:
                        print('多谢大爷打赏，您的物件已被标为快件')
                        print('+'*30)
                        print('本次服务到此结束')

                elif num == 2:
                    buy = input('挑选你要购买的商品名称')
                    if buy == commodity[0]:
                        print('你要购买的商品是：%s'%commodity[0])
    
                        print('输入1,确定购买。。输入2,确认返回')
   
                        num = int(input('请输入命令数字'))
   
                        if num == 1:
                            print('你已经确认购买该商品')
    
                            yuan_jia = 100
                            da_zhe = 100*0.45

                            print('飞科剃须刀的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
                            fu_kuan = int(input('请付款：'))
                            if fu_kuan == da_zhe:
                                print('付款成功，预计三天后和你见面')
                                print('+'*30)
                                print('本次服务到此结束')
                            elif fu_kuan < da_zhe:
                                print('支付金额不够，有钱了再来，将为你自动退出')
                                print('+'*30)
                                print('本次服务到此结束')
                            else:
                                print('多谢大爷打赏，您的物件已被标为快件')
                                print('+'*30)
                                print('本次服务到此结束')
                        else:
                            pass
            elif buy == commodity[0]:
                print('你要购买的商品是：%s'%commodity[0])

                print('输入1,确定购买。。输入2,确认返回')

                num = int(input('请输入命令数字'))

                if num == 1:
                    print('你已经确认购买该商品')

                    yuan_jia = 100
                    da_zhe = 100*0.45

                    print('飞科剃须刀的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
                    fu_kuan = int(input('请付款：'))
                    if fu_kuan == da_zhe:
                        print('付款成功，预计三天后和你见面')
                        print('+'*30)
                        print('本次服务到此结束')
                    elif fu_kuan < da_zhe:
                        print('支付金额不够，有钱了再来，将为你自动退出')
                        print('+'*30)
                        print('本次服务到此结束')
                    else:
                        print('多谢大爷打赏，您的物件已被标为快件')
                        print('+'*30)
                        print('本次服务到此结束')

                elif num == 2:
                    buy = input('挑选你要购买的商品名称')
                    if buy == commodity[2]:
                        print('你要购买的商品是：%s'%commodity[2])

                        print('输入1,确定购买。。输入2,确认返回')

                        num = int(input('请输入命令数字'))

                        if num == 1:
                            print('你已经确认购买该商品')

                            yuan_jia = 3000
                            da_zhe = 3000*0.45

                            print('iphone x 的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
                            fu_kuan = int(input('请付款：'))
                            if fu_kuan == da_zhe:
                                print('付款成功，预计三天后和你见面')
                                print('+'*30)
                                print('本次服务到此结束')
                            elif fu_kuan < da_zhe:
                                print('支付金额不够，有钱了再来，将为你自动退出')
                                print('+'*30)
                                print('本次服务到此结束')
                            else:
                                print('多谢大爷打赏，您的物件已被标为快件')
                                print('+'*30)
                                print('本次服务到此结束')
                        else:
                            pass
    elif buy == commodity[2]:
        print('你要购买的商品是：%s'%commodity[2])

        print('输入1,确定购买。。输入2,确认返回')

        num = int(input('请输入命令数字'))

        if num == 1:
            print('你已经确认购买该商品')

            yuan_jia = 3000
            da_zhe = 3000*0.45

            print('iphone x 的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
            fu_kuan = int(input('请付款：'))
            if fu_kuan == da_zhe:
                print('付款成功，预计三天后和你见面')
                print('+'*30)
                print('本次服务到此结束')
            elif fu_kuan < da_zhe:
                print('支付金额不够，有钱了再来，将为你自动退出')
                print('+'*30)
                print('本次服务到此结束')
            else:
                print('多谢大爷打赏，您的物件已被标为快件')
                print('+'*30)
                print('本次服务到此结束')

        elif num == 2:
            buy = input('挑选你要购买的商品名称')
            if buy == commodity[0]:
                print('你要购买的商品是：%s'%commodity[0])

                print('输入1,确定购买。。输入2,确认返回')

                num = int(input('请输入命令数字'))
 
                if num == 1:
                    print('你已经确认购买该商品')
    
                    yuan_jia = 100
                    da_zhe = 100*0.45
  
                    print('飞科剃须刀的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
                    fu_kuan = int(input('请付款：'))
                    if fu_kuan == da_zhe:
                        print('付款成功，预计三天后和你见面')
                        print('+'*30)
                        print('本次服务到此结束')
                    elif fu_kuan < da_zhe:
                        print('支付金额不够，有钱了再来，将为你自动退出')
                        print('+'*30)
                        print('本次服务到此结束')
                    else:
                        print('多谢大爷打赏，您的物件已被标为快件')
                        print('+'*30)
                        print('本次服务到此结束')

                elif num == 2:
                    buy = input('挑选你要购买的商品名称')
                    if buy == commodity[1]:
                        print('你要购买的商品是：%s'%commodity[1])
    
                        print('输入1,确定购买。。输入2,确认返回')
   
                        num = int(input('请输入命令数字'))
   
                        if num == 1:
                            print('你已经确认购买该商品')
    
                            yuan_jia = 200
                            da_zhe = 200*0.45

                            print('耐克运动鞋的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
                            fu_kuan = int(input('请付款：'))
                            if fu_kuan == da_zhe:
                                print('付款成功，预计三天后和你见面')
                                print('+'*30)
                                print('本次服务到此结束')
                            elif fu_kuan < da_zhe:
                                print('支付金额不够，有钱了再来，将为你自动退出')
                                print('+'*30)
                                print('本次服务到此结束')
                            else:
                                print('多谢大爷打赏，您的物件已被标为快件')
                                print('+'*30)
                                print('本次服务到此结束')
                        else:
                            pass
            elif buy == commodity[1]:
                print('你要购买的商品是：%s'%commodity[1])

                print('输入1,确定购买。。输入2,确认返回')

                num = int(input('请输入命令数字'))

                if num == 1:
                    print('你已经确认购买该商品')

                    yuan_jia = 200
                    da_zhe = 200*0.45

                    print('耐克运动鞋的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
                    fu_kuan = int(input('请付款：'))
                    if fu_kuan == da_zhe:
                        print('付款成功，预计三天后和你见面')
                        print('+'*30)
                        print('本次服务到此结束')
                    elif fu_kuan < da_zhe:
                        print('支付金额不够，有钱了再来，将为你自动退出')
                        print('+'*30)
                        print('本次服务到此结束')
                    else:
                        print('多谢大爷打赏，您的物件已被标为快件')
                        print('+'*30)
                        print('本次服务到此结束')

                elif num == 2:
                    buy = input('挑选你要购买的商品名称')
                    if buy == commodity[0]:
                        print('你要购买的商品是：%s'%commodity[0])

                        print('输入1,确定购买。。输入2,确认返回')

                        num = int(input('请输入命令数字'))

                        if num == 1:
                            print('你已经确认购买该商品')

                            yuan_jia = 3000
                            da_zhe = 3000*0.45

                            print('飞科剃须刀的原价是%d元，打四五折，现价是%d元'%(yuan_jia,da_zhe))
                            fu_kuan = int(input('请付款：'))
                            if fu_kuan == da_zhe:
                                print('付款成功，预计三天后和你见面')
                                print('+'*30)
                                print('本次服务到此结束')
                            elif fu_kuan < da_zhe:
                                print('支付金额不够，有钱了再来，将为你自动退出')
                                print('+'*30)
                                print('本次服务到此结束')
                            else:
                                print('多谢大爷打赏，您的物件已被标为快件')
                                print('+'*30)
                                print('本次服务到此结束')
                        else:
                            pass
    tian_jia = input('请输入你要添加的商品')
    commodity.append(tian_jia)
    print('现在的商品有：%s'%commodity)
elif account == name1 and passwd != mi_ma1:
    print("你输入的帐号或密码错误，即将推出淘宝，，请重新进入")
    pass

elif account != name1 and passwd == mi_ma1:
    print('你输入的帐号或密码错误，即将退出淘宝，请重新进入')
    pass

elif account != name1 and passwd != mi_ma1:
    print('你输入的帐号或密码错误，即将退出淘宝，请重新进入')
    pass
