name = input("请输入你的名字")
age = int(input("请输入你的年龄"))
school = input("请输入你的学历")
if age > 18 and school == "初中以上":
    print("恭喜你，你入职了")
elif age > 18 and school != "初中以上":
    print("不好意思，请进入第二轮面试")
elif age <= 18 and school == "初中以上":
    print("不好意思，请进入第二轮面试")
else:
    print("不好意思，你不符合本公司的要求")
