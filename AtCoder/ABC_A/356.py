N, L, R = map(int, input().split())
i = 0
j = 0
ans_arr = []

while i < N:
	if i+1 >= L and i+1 <= R:
		ans_arr.append(R-j)
		j += 1
	else:
		ans_arr.append(i+1)
	i += 1

print(*ans_arr)