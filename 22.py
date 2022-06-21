dict1 = {123:[456,9000],456:[789,5000],789:[888,6000],336:[558,10000],775:[666,12000],566:[221,7000]}
a = int(input("請輸入查詢組數:"))
for i in range(a):
	b = int(input("請輸入帳號:"))
	c = int(input("請輸入密碼"))
	if b == 123 or b == 456 or b == 789 or b == 336 or b == 775 or b == 566:
		if c == dict1.get(b)[0]:
			print(dict1.get(b)[1])
		elif c != dict1.get(b)[0]:
			print("crror")
	else:
		print("crror")


