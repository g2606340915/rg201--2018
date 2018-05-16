def demo(*p):
    print(p)
demo(1,2,3)
print('*'*30)
demo(1,2,3,4,5,6,7)
print('*'*30)
print('第二种可变参数：')
def demo2(**p):
    for item in p.items():
        print(item)

demo2(x=1,y=2,z=3)

