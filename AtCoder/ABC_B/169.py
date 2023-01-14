n = int(input())
a = list(map(int, input().split()))

a_sort = sorted(a, reverse=True)

if a_sort[n-1] == 0:
	print(0)
	exit()
else:
	ans = a_sort[0]
	a_sort.pop(0)
	for i in a_sort:
		ans *= i
		if ans > 1000000000000000000:
			print(-1)
			exit()

print(ans)