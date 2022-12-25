h, w = map(int, input().split())
s = [ list(map(str, input())) for i in range(h) ]

print("")

def b_check(i, j, h, w):
	b_num = 0
	if w >= j+2:
		if s[i][j+1] == "#":#右
			b_num += 1
	if j-1 >= 0:
		if s[i][j-1] == "#":#左
			b_num += 1
	if i-1 >= 0:
		if s[i-1][j] == "#":#上
			b_num += 1
	if h >= i+2:
		if s[i+1][j] == "#":#下
			b_num += 1
	if w >= j+2 and i-1 >= 0:
		if s[i-1][j+1] == "#":#右上
			b_num += 1
	if j-1 >= 0 and i-1 >= 0:
		if s[i-1][j-1] == "#":#左上
			b_num += 1
	if w >= j+2 and h >= i+2:
		if s[i+1][j+1] == "#":#右下
			b_num += 1
	if j-1 >= 0 and h >= i+2:
		if s[i+1][j-1] == "#":#左下
			b_num += 1
	print(b_num, end="")

for i in range(h):
	for j in range(w):
		if s[i][j] == ".":
			b_check(i, j, h, w)
		else:
			print("#", end="")
		if j == w-1:
			print("\n", end="")