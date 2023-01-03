n = int(input())
a = list(map(int, input().split()))
flag = 0
count = 0

while flag == 0:
	a_tmp = a
	for i in range(n):
		if a[i]%2 == 0:
			a[i] /= 2
		else:
			flag = 1
	if flag == 0:
		count += 1

print(count)