num = 1
sheep = "SHEEP"
ans_list = []

for i in range(1, 100000):
	ans_list.append(str(i) + sheep)

ans = ''.join(ans_list)

for i in range(20):
	print(ans[33333+i-1])