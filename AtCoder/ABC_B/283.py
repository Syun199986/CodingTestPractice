n = int(input())
a = list(map(int, input().split()))
q = int(input())
q_list = []

for i in range(q):
	q_list.append(list(map(int, input().split())))

for i in q_list:
	if i[0] == 1:
		a[i[1]-1] = i[2]
	elif i[0] == 2:
		print(a[i[1]-1])