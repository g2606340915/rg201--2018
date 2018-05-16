def say(message,times=1):
    print((message+'')*times)

say.__defaults__
print('*'*30)

say('hello')
print('*'*30)
say('world\n',7)
