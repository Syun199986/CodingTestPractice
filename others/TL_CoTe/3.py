def digitSum(num):
    str_num = str(num)
    num_digit = list(map(int, str_num))
    return sum(num_digit)

num_list = []
count = 0

for i in range(1, 10000000):
	if i % digitSum(i) == 0:
		count += 1

print(count)