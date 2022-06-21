n = int(input("請輸入Peter有幾支菸:"))
k = int(input("請輸入有幾支菸屁股可以捲成一支新的紙菸(k>1):"))
c = 0
if n//k:
	c += n//k
	if c//k:
		c += c//k
print(n+c)