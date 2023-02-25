n, k = map(int, input().split())
s = input()

for i in s:
	if k > 0:
		if i == "o":
			print("o", end="")
			k -= 1
		else:
			print("x", end="")
	else:
		print("x", end="")
