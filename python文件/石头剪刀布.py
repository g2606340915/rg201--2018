import random# 随机函数
guess_list = ["石头","剪刀","布"]
# 胜利的情况
win = [["布","石头"],["石头","剪刀"],["剪刀","布"]]
while True:
    computer = random.choice(guess_list)
    people = input('请输入：石头，剪刀，布\n').strip()
    if people not in guess_list:
        continue
    elif computer == people:
        print("平手，再来一次！")
    elif [computer,people] in win:
        print("电脑获胜，再玩，人获胜才能退出！")
    else:
        print("人获胜！")
        break
