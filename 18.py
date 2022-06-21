sum=0
for i in range(5):
	a = input("請輸入五張牌:")
	if a == "A":
		sum+=1
	elif a == "J":
		sum+=11
	elif a == "Q":
		sum+=12
	elif a == "K":
		sum+=13
	else:
		sum+=int(a)
print(sum)