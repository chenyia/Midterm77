n = int(input("請輸入正整數:"))
sum = 0
for i in range(1,n):
	if n%i == 0:
		sum += i
if n == sum:
	print("perfect")
elif n > sum:
	print("deficient")
elif n < sum:
	print("abundant")