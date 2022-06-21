# 不嚴謹(有誤)



a = int(input("請輸入第一個要判斷的數字:"))
b = int(input("請輸入第二個要判斷的數字:"))
if a%2==0 and b%2==0:
	print("N")
else:
	if b-a == 2:
		print("Y")
	else:
		print("N")

