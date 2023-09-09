n = int(input())
div = []
s = ""
flag = 0

for i in range(1,n+1):
	if i < 10:
		if n % i == 0:
			div.append(i)
	else:
		break

for i in range(0,n+1):
	flag = 0
	for j in div:
		if i % (n / j) == 0:
			s += str(j)
			flag = 1
			break
	if flag == 0:
		s += "-"

print(s)