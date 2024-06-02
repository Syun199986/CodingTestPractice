N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for l in range(N)]

for j in range(M):
	for i in range(N):
		A[j] -= X[i][j]

count_of_no_intake = sum(x>0 for x in A)

if count_of_no_intake == 0: print("Yes")
else: print("No")