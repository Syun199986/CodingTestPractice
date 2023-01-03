n, q = map(int, input().split())
ff_map = [[0 for i in range(n)] for j in range(n)]

q_list = []
for i in range(q):
	q_list.append(list(map(int, input().split())))

for i in q_list:
	if i[0] == 1 and (ff_map[i[1]-1][i[2]-1] != 1):
			ff_map[i[1]-1][i[2]-1] += 1
	elif i[0] == 2 and (ff_map[i[1]-1][i[2]-1] != 0):
			ff_map[i[1]-1][i[2]-1] -= 1
	elif i[0] == 3:
		if (ff_map[i[1]-1][i[2]-1] == 1) and (ff_map[i[2]-1][i[1]-1] == 1):
			print("Yes")
		else:
			print("No")
