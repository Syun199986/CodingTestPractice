n = int(input())
result = 0
for i in range(n):
	if input() == "For":
		result += 1
	else:
		result += -1

if result > 0:
	print("Yes")
else:
	print("No")