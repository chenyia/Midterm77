a = int(input("請輸入要測試的資料量:"))
for i in  range(a) :
	b = input("請輸入父親血型:")
	c = input("請輸入母親血型:")
	d = input("請輸入子女血型:")
	if (b == "O" or c == "O") and (b == "O" or c == "O"):
		if d == "O":
			print("YES")
		else:
			print("IMPOSSIBLE")
	elif (b == "O" or c == "O") and (b == "A" or c == "A"):
		if d == "O" or d == "A":
			print("YES")
		else:
			print("IMPOSSIBLE")
	elif (b == "O" or c == "O") and (b == "B" or c == "B"):
		if d == "O" or d == "B":
			print("YES")
		else:
			print("IMPOSSIBLE")
	elif (b == "O" or c == "O") and (b == "AB" or c == "AB"):
		if d == "A" or d == "B":
			print("YES")
		else:
			print("IMPOSSIBLE")
	elif (b == "A" or c == "A") and (b == "A" or c == "A"):
		if d == "A" or d == "o":
			print("YES")
		else:
			print("IMPOSSIBLE")
	elif (b == "A" or c == "A") and (b == "B" or c == "B"):
		if d == "A" or d == "o" or d == "B" or d =="AB":
			print("YES")
		else:
			print("IMPOSSIBLE")
	elif (b == "A" or c == "A") and (b == "AB" or c == "AB"):
		if d == "A" or d == "B" or d == "AB":
			print("YES")
		else:
			print("IMPOSSIBLE")
	elif (b == "B" or c == "B") and (b == "B" or c == "B"):
		if d == "O" or d == "B":
			print("YES")
		else:
			print("IMPOSSIBLE")
	elif (b == "B" or c == "B") and (b == "AB" or c == "AB"):
		if d == "A" or d == "B" or d == "AB":
			print("YES")
		else:
			print("IMPOSSIBLE")
	elif (b == "AB" or c == "AB") and (b == "AB" or c == "AB"):
		if d == "A" or d == "B" or d == "AB":
			print("YES")
		else:
			print("IMPOSSIBLE")