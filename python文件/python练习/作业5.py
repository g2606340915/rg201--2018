def demo(newitem,old_list=[]):
    old_list.append(newitem)
    return old_list
def printLine():
    print('*'*30)

print(demo('5',[1,2,3,4]))
printLine()
print(demo('aaa',['a','b']))
printLine()
print(demo('a'))
printLine()
print(demo('b'))
