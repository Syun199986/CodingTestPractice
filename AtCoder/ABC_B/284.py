t = int(input())
ans_list = []
for i in range(t):
	ans = 0
	n = input()
	a = list(map(int, input().split()))
	for j in a:
		if j%2 == 1:
			ans += 1
	ans_list.append(ans)

for i in ans_list:
	print(i)