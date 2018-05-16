# 完成5行内容的简单输出
# 分析每一行*应该如何处理？ 每行显示的*和当前所在的行数是一致
'''
row = 1
while row<=5:
    col = 1
    while col <= row:
        print('、',end='')
        col += 1
    print("")
    row += 1
'''

row = 1
while row <= 9:
    col = 1
    while col+1 <= row:
        print("%d*%d=%d"%(col,row,col*row),end="\t")
        col += 1
    print("%d*%d=%d"%(row,col,row*col))
    row += 1
