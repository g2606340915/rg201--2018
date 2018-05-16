# 房屋销售
print("       ")
print("*" * 40)
print("       ")
print("欢迎来到“王者荣耀”线上售楼站")
print("我们将为您献上最周到的服务")
print("       ")
print("       ")
print("目前只有北京和山西两个城市的楼房可购")
print("       ")
place = input("您所购的房子的城市")
if place == "北京":
    price = int(input("您能接受的房价"))
    if price >= 5000:
        print("您好，已为您找到房源")
        print("联系人：武则天，联系电话：12345678998")
    else:
            print("滚，穷比")
elif place == "山西":
    price = int(input("您能接受的房价"))
    if price >= 50000:
        print("您好，欢迎购买最美山西的楼房")
        print("联系人：马化腾，联系电话：88888888888")
    else:
        print("滚，大穷比，连五万都没有")
