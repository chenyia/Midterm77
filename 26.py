while True:
	a = str(input("請輸入要檢測的字串(end 結束):"))
	if a=="end":
		print("測驗結束")
		break
	else:
		b = str(input("請輸入檢測的單一字元:"))
		c=a.count(b)
		print("字元",b,"出現次數為:",c)

