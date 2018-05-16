'''
# a = 3
def test1():
    global a
    a = 1
    print(a)

def test2():
    #global a
    a = 2
    print(a)  

test1()
print('-'*30) 
test2()
print('-'*30) 
print(a)
'''
a = {'姓名':'小明'}
def test1():
    # global a 
    a['姓名'] = ('小红')
    print(a)


test1()


