# 串列
n = int(input("請輸入整數(0<n<1000000):"))
a = list()
while n > 1:
	if n%2 == 1:
		n = 3*n+1
		a.append(n)
	else:
		n = n/2
		a.append(n)
print("數列:",a)


# 
n = int(input("請輸入整數(0<n<1000000):"))
print(n)
while n > 1:
	if n%2 == 1:
		n = 3*n+1
		print(n)
	else:
		n = n/2
		print(n)
