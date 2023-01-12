s = int(input())
s_list = [int(x) for x in list(str(s))]

ans = 0
i = 0

while i < len(s_list):
	if s_list[i] == 0 and i < len(s_list)-1:
		if s_list[i+1] == 0:
			i += 2
		else:
			i += 1
	else:
		i += 1
	ans += 1

print(ans)