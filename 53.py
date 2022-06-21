dict1={}
a=int(input("輸入幾筆資料:"))
for i in range(a):
	name = input("請輸入姓名:")
	email = input("請輸入電子郵件:")
	dict1[name]=email
k = input("請輸入要查詢電子郵件的姓名:")
print(k,"電子郵件帳號為",dict1.get(k))
