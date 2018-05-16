"""
商品名：黄瓜
单价：2
重量：3
实付：10
找零：4
"""

name = input("请输入商品名称")
price = float(input("请输入商品单价"))
weight = float(input("请输入商品重量"))
sum = price * weight

print("应付:%s"%sum)
pay = float(input("收款:"))
if pay >= price * weight:
    different = int(pay)-sum
    print("找零:"+str(different))
else:
    print("钱不够，回家带钱")
