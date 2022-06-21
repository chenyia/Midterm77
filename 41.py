m = 0
T = int(input("搭了幾次電梯:"))
a = input("到達樓層:")
b = list(a.split(" "))
if int(b[0])>1:
	m += (int(b[0])-1)*20
if int(b[1])>int(b[0]):
	m += (int(b[1])-int(b[0]))*20
else:
	m += (-(int(b[1])-int(b[0])))*10
if int(b[2])>int(b[1]):
	m += (int(b[2])-int(b[1]))*20
else:
	m += (-(int(b[2])-int(b[1])))*10
if int(b[3])>int(b[2]):
	m += (int(b[3])-int(b[2]))*20
else:
	m += (-(int(b[3])-int(b[2])))*10
if int(b[4])>int(b[3]):
	m += (int(b[4])-int(b[3]))*20
else:
	m += (-(int(b[4])-int(b[3])))*10
print(m,"元")

#可以用更有效率的方法

