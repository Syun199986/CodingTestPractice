ans_list = []
tmp = 1
count = 0

while tmp <= 1111111:
    ans_list.append(str(7*tmp))
    tmp += 1

for i in ans_list:
    for j in i:
        if j == "7":
            count += 1

print(count)