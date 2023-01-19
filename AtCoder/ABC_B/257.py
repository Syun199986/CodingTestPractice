n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))
top_pawn = len(a)

for i in l:
	if i == top_pawn:
		if n > a[i-1]:
			a[i-1] += 1
	else:
		if a[i]-1 > a[i-1]:
			a[i-1] += 1

for i in a:
	print(i, end=" ")