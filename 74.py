a = ["red","blue","red","green"]
n = 0
while n<10:
	color = input("請依序輸入四個顏色(中間以空白間隔):")
	n += 1
	if n == 10 and color != "red blue red green":
		print("挑戰失敗")
		break
	else:
		if color == "red blue red green":
			print("正確答案")
			break
		else:
			b = ""
			c = color.split()
			for i in range(len(c)):
				if a[i]==c[i]:
					b += "1"
				elif a[i]!=c[i] and a.count(c[i])>0:
					b += "2"
				else:
					b += "3"
			print(b)
