# 先假设电脑只会出石头   石头代表：1
computer = 1
player = int(input("请输入你的拳头"))
if player == 2:
    print("电脑赢了")
elif player == 3:
    print("人赢了")
else:
    print("平手")
