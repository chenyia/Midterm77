while True:
	a = int(input("請輸入組數:"))
	for i in range(1,a+1):
		b=list(input("輸入購買全票半票張數:"))
		c=int(b[0])*250+int(b[1])*175
		print("第",i,"組應收費用:",c)
	break
