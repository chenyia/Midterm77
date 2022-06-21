a = input("請輸入第一組數字:")
b = input("請輸入第二組數字:")
acount=0
bcount=0
for i in a:
	for j in b:
		if i == j:
			if a.index(i)==b.index(j):
				acount+=1
			else:
				bcount+=1
if acount==4 and bcount==0:
	print(str(acount)+"A"+str(bcount)+"B","全對")
else:
	print(str(acount)+"A"+str(bcount)+"B","加油")