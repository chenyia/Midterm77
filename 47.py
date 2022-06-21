n = int(input("請輸入筆數:"))
for i in range(n):
	a = input("請輸入獎牌名稱及數量(金 4):")
	b = a.split(" ")
	print("%s牌得到%s面"%(b[0],b[1]))