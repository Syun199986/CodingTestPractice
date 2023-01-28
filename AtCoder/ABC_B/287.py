n, m = map(int, input().split())
s = []
t_list = []
ans = 0

for i in range(n):
	s.append(input())
for i in range(m):
	t_list.append(input())

t = list(set(t_list))

for i in t:
	for j in range(len(s)):
		if i[0] == s[j][3]:
			p = 3 # s[j][p]
			q	= 0 # i[q] → Tの文字列のi番目
			while s[j][p] == i[q]:
				if p == 5 and q == 2:
					ans += 1
					break
				p += 1
				q += 1

print(ans)