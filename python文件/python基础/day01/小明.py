name = input("姓名：")
hight = float(input("身高："))
weight = float(input("体重："))
BMI = weight / (hight **2)
if BMI < 18.5:
    print("%s的BMI指数为%s，过轻"%(name,BMI))
elif BMI >= 18.5 and BMI <= 25:
    print("%s的BMI指数为%S，正常"%(name,BMI))
elif BMI > 25 and BMI <= 28:
    print("%s的BMI指数为%s，过重"%(name,BMI))
elif BMI > 28 and BMI <= 32:
    print("%s的BMI指数为%s，肥胖"%(name,BMI))
else:
    print("%s的BMI指数为%s，严重肥胖"%(name,BMI))
