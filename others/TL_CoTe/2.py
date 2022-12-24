ans_list = []
num_list = []

for i in range(1, 12346, 3):
	num_list.append(i)
	ans_list.append(i * (i+1) / (i+2))

print(int(sum(ans_list)))