#一次元オセロ

# 標準入力
std_in = "RLLRLRRLRL"

# answer_field
ans_f = ["b", "w"]

# answer_fieldの右端に引数の色を置いて、置いた位置を返す
def R(color):
	ans_f.append(color)
	return (len(ans_f) - 1)

# answer_fieldの左端に引数の色を置いて、置いた位置を返す
def L(color):
	ans_f.insert(0, color)
	return 0

# 入力がRの場合の処理
def R_check(color):
	# 引数のcolorをfront(表)、もう一方をback(裏)にする
	if color == "b":
		front = "b"
		back = "w"
	elif color == "w":
		front = "w"
		back = "b"
	# 右に置いて、現在地(current_position)をセット
	cp = R(front)
	# 置いた場所の左隣がbackかどうか判別
	if ans_f[cp-1] == back:
		# 探索し始めた位置をcp_tmpに保存しておく
		cp_tmp = cp
		cp -= 1
		# 左向きにbackである限り探索を続ける
		while ans_f[cp] == back:
			cp -= 1
		# 左端まで探索が進んだ場合は色を変化させない( = 挟むための色がなかった場合)
		if cp != -1:
			for i in range(cp_tmp, cp-1, -1):
				ans_f[i] = front

# 入力がLの場合の処理
def L_check(color):
	# 引数のcolorをfront(表)、もう一方をback(裏)にする
	if color == "b":
		front = "b"
		back = "w"
	elif color == "w":
		front = "w"
		back = "b"
	# 左に置いて、現在地(current_position)をセット
	cp = L(front)
	# 置いた場所の右隣がbackかどうか判別
	if ans_f[cp+1] == back:
		# 探索し始めた位置をcp_tmpに保存しておく
		cp_tmp = cp
		cp += 1
		# 右向きにbackである限り探索を続ける
		while ans_f[cp] == back:
			cp += 1
			# リスト外参照の防止
			if cp == len(ans_f):
				break
		# 右端まで探索が進んだ場合は色を変化させない( = 挟むための色がなかった場合)
		if cp != len(ans_f):
			for i in range(cp_tmp, cp+1):
				ans_f[i] = front

for i in range(len(std_in)):
	# 黒の番(偶数回目)
	if i%2 == 0:
		if std_in[i] == "R":
			R_check("b")
		elif std_in[i] == "L":
			L_check("b")
	# 白の番(奇数回目)
	elif i%2 == 1:
		if std_in[i] == "R":
			R_check("w")
		elif std_in[i] == "L":
			L_check("w")

print(str(ans_f.count("b")) + " " + str(ans_f.count("w")))