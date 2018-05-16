class di_gua:
    def __init__(self):
        self.cookLever = 0
        self.cookStr = '生的'
        self.pei_liao = []


def cook(self,time):
    self.cookLever += time
    if self.cookLever > 8:
        self.cookStr = '烤成炭了'
    elif self.cookLever > 5:
        self.cookStr = '烤好了'
    elif self.cookLever > 3:
        self.cookStr = '半生不熟'
    else:
        self.cookSTr = '生的'

def __str__(slef):
    

kao_di_gua = di_gua()
print(kao_di_gua.cookLever)
print(kao_di_gua.cookStr)
print(kao_di_gua.pei_liao)


