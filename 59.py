a = int(input("請輸入金額:"))
b = (a//100)+(a%100//50)+ (a%50//10)+(a%10//5)+(a%5//1)
print(b)