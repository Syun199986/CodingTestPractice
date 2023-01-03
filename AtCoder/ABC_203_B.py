n, k = map(int, input().split())
ans = 0

for i in range(100, n*100+100, 100):
	for j in range(1, k+1):
		ans += i+j

print(ans)