row = 1
while row <= 9:
    col = 1
    while col+1 == row:
        print('%d*%d=%d'%(col,row,col*row),end='\t')
        col += 1
    row += 1
