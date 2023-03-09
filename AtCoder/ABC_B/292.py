n, q = map(int, input().split())
e = []
e_flag = []
for i in range(q):
	e.append(list(map(int, input().split())))

for i in range(n):
	e_flag.append(0)

for i in e:
	if i[0] == 1:
		e_flag[i[1]-1] += 1
	elif i[0] == 2:
		e_flag[i[1]-1] += 2
	else:
		if e_flag[i[1]-1] >= 2:
			print("Yes")
		else:
			print("No")