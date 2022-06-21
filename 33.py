# 不完整 缺科目
list1=[]
sum = 0
max = 0
min = 100
for i in range(5):
	S = int(input("成績(0<=S<=100):"))
	list1.append(S)
	sum+=list1[i]
	if max < list1[i]:
		max = list1[i]
	if min > list1[i]:
		min = list1[i]
print("平均分數%2.2f"%(sum/5))
print("最高分科目:",max,"分")
print("最低分科目:",min,"分")



