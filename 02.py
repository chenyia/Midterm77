d = int(input("請輸入度數(正整數)"))
if d <= 120:
	print("Summer months:",round(d*2.10,2),"Non-Summer months:",round(d*2.10,2))
elif d > 120 and d <= 330:
	print("Summer months:",round(d*3.02,2),"Non-Summer months:",round(d*2.68,2))
elif d > 330 and d <= 500:
	print("Summer months:",round(d*4.39,2),"Non-Summer months:",round(d*3.61,2))
elif d > 500 and d <= 700:
	print("Summer months:",round(d*4.97,2),"Non-Summer months:",round(d*4.01,2))
else:
	print("Summer months:",round(d*5.63,2),"Non-Summer months:",round(d*4.50,2))