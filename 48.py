dict1={}
n = int(input("請輸入筆數:"))
for i in range(n):
	a =input("請輸入英文:")
	b =input("請輸入中文:")
	dict1[a]=b
k = input("請輸入欲查詢單字:")
print(k,"中文意思為",dict1.get(k))