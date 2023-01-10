n, m = map(int, input().split())
a = list(map(int, input().split()))

able_to_play = n - sum(a)

if able_to_play < 0:
	print(-1)
else:
	print(able_to_play)