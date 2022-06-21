# 不完整
a = list(input("請輸入一組四位整數數字:"))
#a=list("1234")
c =""
for i in range(len(a)):
		b = str((int(a[i])+7)%10)
		c += b
d =list(c)
d[0],d[2] = d[2],d[0]
d[1],d[3] = d[3],d[1]
print(d)


