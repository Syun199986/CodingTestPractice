n = int(input())
a = list(map(int, input().split()))

pizza = [0] * 360
pizza[0] = 1
next_pos = 0
max_num = 0

for i in a:
	next_pos += i
	if next_pos >= 360:
		next_pos -= 360
	pizza[next_pos] = 1

pizza.append(1)
i = 0

while i < 360:
	count = 0
	if pizza[i] == 1:
		count = 1
		while pizza[i+1] == 0:
			count += 1
			i += 1
		if max_num < count:
			max_num = count
	i += 1
	
print(max_num)