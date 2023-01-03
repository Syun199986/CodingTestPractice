def digitSum(num):
	str_num = str(num)
	int_num = list(map(int, str_num))
	return sum(int_num)

n, a, b = map(int, input().split())
ans = 0

for i in range(1, n+1):
	num = digitSum(i)
	if (num >= a) and (num <= b):
		ans += i

print(ans)