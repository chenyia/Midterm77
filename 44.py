
"""
#T = int(input("有幾班任教班級(1<=T<=10):"))
T=5
for i in range(T):
#	a = int(input("班級人數:"))
	a =[42,39,41,43,30]
#	list1 = [a]
	for j in range(T):
		if a[j]>=a[j-i-1]:
			b = a[j]
		else:
			b = a[j-i-1]
print(b)
"""

# 錯誤
T = int(input("有幾班任教班級(1<=T<=10):"))
max = 0
for i in range(T):
	a = (input("班級人數:"))
	list1 = []
	list1.append(a)
	for j in range(T):
		if a[j]>a[j-i-1]:
			max = a[j]
print(max)

