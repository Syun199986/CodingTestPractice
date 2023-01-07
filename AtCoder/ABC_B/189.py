n, x = map(int, input().split())
a = []
a_sum = 0
a_flag = 0
count = 1

for i in range(n):
	a.append(list(map(int, input().split())))

for i in a:
	a_sum += i[0]*i[1]
	if a_sum > x * 100:
		a_flag = 1
		break
	count += 1

if a_flag == 1:
	print(count)
else:
	print(-1)