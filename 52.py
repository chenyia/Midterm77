a = list("紅豆生南國,春來發幾枝?願君多采擷,此物最相思。")
b = list("春眠不覺曉,處處聞啼鳥。夜來風雨聲,花落知多少。")
c = ""
for i in range(len(a)):
	for j in range(len(b)):
		if a[i]==b[j] :
			c += a[i]
d = list(set(c))
d.remove(",")
d.remove("。")
print(d)
