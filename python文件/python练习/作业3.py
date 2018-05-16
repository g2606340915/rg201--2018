# 某些情况下是可以修改实参的
def modify(m):
    m[0] = m[0]+1
    return m 
a = [2]
print(modify(a))
print(a)

print('*'*30)


def modify2(m,item):
    m.append(item)
    return m

b = [4]
print(modify2(b,5))
print(b)

print('*'*30)
'''
def modify3(c):
    c['age'] = 38
    
b = [4]
print(modify3)
print(b)
'''
print('*'*30)

def modify4(d):
    d['age'] = 38
d = {'name':'李文浩','age':18}
print(d)

