n, l = map(int, input().split())
taste_list = []

for i in range(1, n+1):
	taste_list.append(l+i-1)

taste_list.remove(min(taste_list, key=abs))
print(sum(taste_list))