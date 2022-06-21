a = list(input("請輸入自傳(至少10個字):"))
b = ""
for i in range(len(a)):
	for j in range(len(a)):
		if a[i]==a[j] :
			b += a[i]
c = list(set(b))
c.remove(",")
c.remove("。")
print(c)