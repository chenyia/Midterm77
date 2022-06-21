ps=list(input("請輸入傳送密碼:"))
a=""
if len(ps)==6:
	for i in ps:
		for j in range(1,10):
			if j*4%7 == int(i):
				a+=str(j)
				break
	print("解密後的密碼:",a)
else:
	ps = list(input("請重新輸入密碼(六位數)"))