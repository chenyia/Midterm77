a = list()
for i in range(10):
	b = input("請輸入十個數字:")
	a.append(b)
	a.sort()
	a.reverse()
print("最大的3個數字為:",a[0],a[1],a[2])	
print("最小的3個數字為:",a[7],a[8],a[9])
