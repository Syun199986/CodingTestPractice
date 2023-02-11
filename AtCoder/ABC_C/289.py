import itertools

n, m = map(int, input().split())
c = []
for i in range(m):
	tmp = int(input())
	c.append(set(map(int, input().split())))

ans_set = set()
for i in range(1, n+1):
	ans_set.add(i)

set_num = []
set_list = []
for i in range(m):
	set_num.append(i)
for i in range(1, m+1):
	set_list += list(itertools.combinations(set_num, i))

ans = 0
for i in set_list:
	check_set = set()
	for j in i:
		check_set.update(c[j])
	if check_set == ans_set:
		ans += 1

print(ans)