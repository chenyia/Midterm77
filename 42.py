a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
x1=(-b+(b**2-4*a*c)**(0.5))/(2*a)
x2=(-b-(b**2-4*a*c)**(0.5))/(2*a)
if b**2-4*a*c<0:
	print("0")
elif b**2-4*a*c>0:
	print(x1,x2)
elif b**2-4*a*c==0:
	print(x1)