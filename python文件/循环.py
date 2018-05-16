# 需求是计算0～100之间所有数字

sum = 0
i = 0
while i <= 100:
    sum = sum + i 
    i += 2
print('最后偶数的和是%d'%sum)

sum = 0 
i = 0
while i <= 100:
    if i%2 == 0:
        sum = sum + i
    i = i +1
print('最后偶数的和是%d'%sum)
























