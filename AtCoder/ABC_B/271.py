n, q = map(int, input().split())
La = []
st = []
ans = []

for i in range(n):
	La.append(list(map(int, input().split())))

for i in range(q):
	st.append(list(map(int, input().split())))

for i in st:
		print(La[i[0]-1][i[1]])