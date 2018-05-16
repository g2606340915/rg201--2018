names = []
while True:
    print('1、添加\t2、查找\t3、删除')

    num = int(input('请输入功能序号'))

    if num == 1:
        name = input('请输入你要添加的姓名')
        names.append(name)
        print('添加成功,有%s'%names)
        
    elif num == 2:
        find_name = input('请输入你要查找的名字')
        if find_name in names:
            print('查到你要找的人')
        else:
            print('未找到')

    elif num == 3:
        name = input('请输入你要删除的名字')
        if name in names:
            names.remove(name)
            print('删除成功,还有%s'%names)
        else:
            print('未找到')

    else:
        print('未找到功能项')
        break   
