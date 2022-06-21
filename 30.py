ans = input("請輸入假設的答案:")
while True:
	a = input("請猜數字:")
	if a == "0000":
		break
	else:
		acount = 0
		bcount = 0
		for i in ans:
			for j in a:
				if i == j:
					if a.index(j) == ans.index(i):
						acount += 1
					else:
						bcount += 1
		print(str(acount)+"A"+str(bcount)+"B")
