has_ticket = int(input("请输入是否有票"))

if has_ticket == True: # 表示有车票
    print("可以进入安检程序")
    knife_length = float(input("请输刀的长度"))
    if knife_length >= 20:
        print("不允许上车")
    else:
        print("可以上车")
else:
    print("请去购买车票")

