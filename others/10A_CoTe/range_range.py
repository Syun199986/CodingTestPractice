def main(lines):

		# n,a[i],qの取得
    n = int(lines[0])
    a = list(map(int, lines[1].split()))
    q = int(lines[2])
		# クエリのリスト保存用のリスト(2次元配列)
    q_list = []
		# クエリ2のカウント用変数
    count = 0

		# クエリの部分のみをリストに保存
    for i in range(3, len(lines)):
        q_list.append(list(map(int, lines[i].split())))

		# クエリの処理
    for i in q_list:
        count = 0
				# クエリ1の処理
        if i[0] == 1:
            a[i[1]-1] = i[2]
				# クエリ2の処理
        elif i[0] == 2:
            for j in range(i[1]-1, i[2]):
                if a[j] >= i[3] and a[j] <= i[4]:
                    count += 1
            print(count)

lines = ['3', '3 1 5', '3', '2 1 3 1 1000', '1 2 10000', '2 1 3 1 1000']
print(main(lines))