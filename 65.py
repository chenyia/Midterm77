a = input("請輸入A的好友:")
b = input("請輸入B的好友:")
c = 0
d = list(a.split(" "))
e = list(b.split(" "))
for i in range(len(d)):
	for j in range(len(e)):
		if d[i] == e[j]:
			c+=1
print(c)