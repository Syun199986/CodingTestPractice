n, t = map(int, input().split())
a = list(map(int, input().split()))
i = 0

while i < n:
	t -= a[i]
	if t < 0:
		t += a[i]
		i += 1
		break
	i += 1
	if i == n:
		i = 0
	
print(str(i) + " " + str(abs(t)))