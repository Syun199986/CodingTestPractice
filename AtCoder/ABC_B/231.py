n = int(input())
cand_dict = {}

for i in range(n):
	cand = input()
	if cand in cand_dict.keys():
		cand_dict[cand] += 1
	else:
		cand_dict.setdefault(cand, 1)

print(max(cand_dict, key=cand_dict.get))