s = input()
t = input()
i = 0
j = 0

while i < len(s):
	if s[i] == t[0]:
		while s[i] == t[j]:
			if j+1 == len(t):
				print("Yes")
				exit()
			i += 1
			j += 1
			if i > len(s)-1:
				print("No")
				exit()
	else:
		i += 1
	if j > 0:
		j = 0

print("No")