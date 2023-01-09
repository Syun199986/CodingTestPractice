s = input()

# seen from the front
sff = [0]*7

if s[0] == "0":
	if s[6] == "1":
		sff[0] = 1
	if s[3] == "1":
		sff[1] = 1
	if s[1] == "1" or s[7] == "1":
		sff[2] = 1
	if s[4] == "1":
		sff[3] = 1
	if s[2] == "1" or s[8] == "1":
		sff[4] = 1
	if s[5] == "1":
		sff[5] = 1
	if s[9] == "1":
		sff[6] = 1
else:
	print("No")
	exit()

for i in range(0, 5):
	for j in range(i+2, 7):
		if sff[i] == 1 and sff[j] == 1:
			for k in range(i+1, j):
				if sff[k] == 0:
					print("Yes")
					exit()

print("No")