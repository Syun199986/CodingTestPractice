count = 1
w = 0
i = 600

while i > 0:
	w += i
	if 5000 >= w:
		i -= 1
	elif 5000 < w:
		count += 1
		w = 0

print(count)