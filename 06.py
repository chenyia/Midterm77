a = list(input("請輸入數值(1<=長度<=7):"))
a.sort()
min=""
for i in range(len(a)):
	min+=a[i]
a.reverse()
max=""
for i in range(len(a)):
	max+=a[i]
res=int(max)-int(min)
print("最大值數列與最小值數列差值為:",res)