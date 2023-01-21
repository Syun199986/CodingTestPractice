n = int(input())
s = input()
ans_list = []
i = 1

while i < n:
	if s[i-1] == "n" and s[i] == "a":
		ans_list.append("nya")
		i += 1
	else:
		ans_list.append(s[i-1])
	i += 1

if i == n:
	ans_list.append(s[n-1])

ans = ''.join(ans_list)

print(ans)