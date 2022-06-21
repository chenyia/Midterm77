#a=input("請輸入一串小寫英文:")
#for i in range(len(a)):
#	b=a.replace('a','.')
#	b=a.replace('e','.')
#	b=a.replace('i','.')
#	b=a.replace('o','.')
#	b=a.replace('u','.')
#print(b)


"""
a=input("請輸入一串小寫英文:")
b=list(a)
c=""
for i in range(len(a)):
	if b[i] == "a":
		a.replace('a','.')
		c+=str(b[i])
	elif a[i] == "e":
		a.replace('e','.')
		c+=str(b[i])
	elif a[i] == "i":
		a.replace('i','.')
		c+=str(b[i])
	elif a[i] == "o":
		a.replace('o','.')
		c+=str(b[i])
	elif a[i] == "u":
		a.replace('u','.')
		c+=str(b[i])
	else:
		c+=str(b[i])
print(c)
"""

"""
#a=list(input("請輸入一串小寫英文:"))
a=list("google")
b=""
for i in range(len(a)):
	if a[i] =="a" and a[i] =="e" and a[i] =="i" and a[i] =="o" and a[i] =="u":
		c=str(a).replace(a[i],".")
		b+=c
	else:
		b+=a[i]
print(b)
"""




