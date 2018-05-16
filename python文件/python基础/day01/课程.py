class1 = int(input("请填写你的语文成绩"))
if class1 >= 60:
    print("通过")
    class2 = int(input("请填写你的数学成绩"))
    if class2 < 60:
        print("你需要补考")
else:
    print("未通过")


