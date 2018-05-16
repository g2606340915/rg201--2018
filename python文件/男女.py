sex = input("你是男，是女，还是其他：")
if sex == "男":
    high = input("你高吗？")
    money = input("你富吗？")
    handsome = input("你帅吗？")
    if high != "矮" and money != "穷" and handsome != "挫":
        print("高富帅")
    else:
        print("矮穷挫")
elif sex == '女':
    color = input("你白吗？")
    money = input("你富吗？")
    beautiful = input("你美吗？")
    if color == '白' or money == '富' or beautiful == '美':
        print('白富美')
else:
    die = input("死还是活")
    if not die == '活':
        print("死人妖")
    else:
        print("活人妖")
