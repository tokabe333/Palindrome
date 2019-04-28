import sys

def main(hantei):
	#入力された100桁の数字が順にvに入る
	for index,v in enumerate(hantei):
		print("hantei({}: {}".format(index,v))
		#vは100桁の数字だが，便宜上text1とする
		text1 = v
		#回文候補を格納
		num0 = []
		#反転させた回文候補を格納
		num1 = []
		#数字の桁数
		length = len(text1)

		#回分候補をnum0に格納
		for i in range(length,2,-1):
			for j in range(0,length + 1 - i):
				num0.append(text1[j:j+i])
			#End_For
		#End_For
		print(num0)

		#回分候補の反転を格納
		for num in num0:
			num1.append(num[::-1])
			##文字列のままではスワップしにくいのでリストにする
			#num = list(num)
			##奇数のとき
			#if len(num) % 2 == 1:
			#	for i in range(int(len(num) % 2)):
			#		tmp = num[i]
			#		num[i] = num[-i]
			#		num[-i] = tmp
			#	#End_For
			#else:
			#	for i in range(len(num) % 2):
			#		tmp = num[i]
			#		num[i] = num[-i]
			#		num[-i] = tmp
			#	#End_For
			##End_IfElse
			##numを文字列になおす
			#num = "".join(num)
			##num1にnumを追加
			#num1.append(num)
		#End_For
		print(num1)

		#回文判定を行う
		for i in range(len(num0)):
			if num0[i] == num1[i]:
				print("最長の回文 : {}".format(num0[i]))
				exit(0)
			#End_If
		#End_For
		print("回文が見つかりませんでした")
	#End_For
#End_Def

if __name__ == "__main__":
	#おそらく100桁の数字が複数入力される
	hantei = []
	for p in sys.stdin:
		hantei.append(p.rstrip("\r\n"))
	main(hantei)