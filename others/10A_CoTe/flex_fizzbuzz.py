# 標準入力テスト
lines = ['3:Fizz 5:Buzz 1']

# 素数判定
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i, v in enumerate(lines):

    # 標準入力をスペース区切りで取得
    stdin_sprit = lines[0].split()

    # mの値を取得
    m = int(stdin_sprit[len(stdin_sprit)-1])

    # 割り切れたa[i]保存用のリスト
    mod_0 = []
    # ":"区切りのリスト保存用リスト(2次元配列)
    sep = []
    # ":"で区切ったリストを登録する辞書
    dict = {}
    # 最終的な文字連結用の変数
    ans = ""

    # linesの文字列をスペース区切りで区切った後にdictに保存
    for i in range(len(stdin_sprit)-1):
        sep.append(stdin_sprit[i].split(":"))
        dict[int(sep[i][0])] = sep[i][1]

    # mで割り切れたa[i]をmod_0に保存
    for i in dict:
        if m % i == 0:
            mod_0.append(i)

    # 割り切れたa[i]が存在したかチェック
    if len(mod_0) == 0:
        if m == 1:
            print(1)
        else:
            # 素数判定
            if is_prime(m) == True:
                print("prime")
            elif is_prime(m) == False:
                print(m)
    # 割り切れたa[i]があった場合、a[i]を小さい順にソートし、valueをansに連結させて出力
    else:
        mod_0.sort()
        for i in mod_0:
            ans += dict[i]
        print(ans)
