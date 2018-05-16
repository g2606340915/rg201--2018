L = []
for i in range(100,1001):
	mark = 0
	for j in range(2,i):
		if i%j == 0:
			mark = 1
			break
	if mark == 0:
		L.append(i)
print(L)
