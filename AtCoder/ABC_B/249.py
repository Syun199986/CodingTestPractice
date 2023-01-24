s = input()
s_set = ''.join(sorted(set(s), key=s.index))
flag = 0

if s == s_set:
	for i in s:
		if i.isupper():
			flag += 1
			break
	for i in s:
		if i.islower():
			flag += 1
			break
	if flag == 2:
		print("Yes")
	else:
		print("No")
else:
	print("No")