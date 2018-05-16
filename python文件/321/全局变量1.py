a = 1
def n():
    a = 3
    print(a)

def m():
    global a
    a += 2
    print(a)
n()
print(a)
m()
print(a)
