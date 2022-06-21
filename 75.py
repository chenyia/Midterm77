
"""
while True:
	a = input("請輸入待辦事項(若已無事項，請輸入end):")
	if a == "end":
		break
	else:
		for i in range(len(a)):
			b = str(i+1)+a
		print(b)
"""
# 仍須思考 
while True:
	a = input("請輸入待辦事項(請以空白區隔待辦事項)(若已無事項，請輸入end):")
	b = a.split(" ")
	d =""
	if a == "end":
		break
	else:
		for i in range(len(b)):
			c = str(i+1)+b[i]
			d += c
		print(d)


# 有誤
while True:
	a = input("請輸入待辦事項(請以空白區隔待辦事項)(若已無事項，請輸入end):")
	b = a.split(" ")
	d =""
	if a == "end":
		break
for i in range(len(b)):
	c = str(i+1)+b[i]
	d += c
print(d)


