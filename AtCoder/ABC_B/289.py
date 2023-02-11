n, m = map(int, input().split())
a = list(map(int, input().split()))
i = 1
j = 0

if m != 0:
	while i <= n:
		back_count = 0
		if j == m:
			for k in range(i, n+1):
				print(str(k) + " ", end="")
			exit()
		if a[j] == i:
			while a[j] == i:
					i += 1
					j += 1
					back_count += 1
					if j > m-1:
						break
			for k in range(back_count + 1):
				print(str(i) + " ", end="")
				i -= 1
			i += 2 + back_count
		else:
			print(str(i) + " ", end="")
			i += 1
else:
	for k in range(1, n+1):
		print(str(k) + " ", end="")