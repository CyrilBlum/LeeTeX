


n = 30031
for k in range(2,n):
	if (n % k == 0):
		p1 = k
		break
p2 = int(n / p1)
print(n,'=', p1, '*',p2)
