'''
l = []
a = [x for x in range(1,100) if x%2 != 0]
l.append(a)
b = [y for y in range(2,100) if y%2 == 0]
l.append(b)
c = [z for z in range(3,100) if z%3 == 0]
l.append(c)
print(l)
'''


'''
d = [[x,x+1,x+2] for x in range(1,100,3)] # for y in range(2,100,3) for z in range(3,100,3)]
print(d)
'''
'''
l = []
for x in range(1,101):
    l.append(x)    
print('l=',l)
'''
'''
v = [x for x in range(1,101) if x%2 != 0]
print(v)
'''
d = [(x,x+1,x+2) for x in range(1,100,3)]
print(d)
