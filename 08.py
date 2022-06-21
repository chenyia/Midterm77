# 不完整

a = int(input("請輸入正整數:"))
b = list()
for i in range(a):
	c = input("請輸入數列數字:")
	b.append(c)
d = set(b)
if len(b) == len(d):
	print("每個數字剛好只出現1次")
else:
	print("數字有重複")



