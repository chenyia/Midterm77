A ={"飢餓遊戲3":1,"解憂雜貨店":2,"怪獸與牠們的產地":3,"哈利波特6":4,"我的阿富汗筆友":5,"祈念之樹":6,"樓下的房客":7,"小王子":8}
B ={"房思琪的初戀樂園":1,"等一個人咖啡":2,"鬼滅之刃14":3,"神農嘗百草":4,"麥田插手":5,"老人與海":6,"傲慢與偏見":7,"與神同行":8}
a = input("請輸入欲租借的書籍:")
if a in A:
	print("在書架A的第",A.get(a),"本")
elif a in B:
	print("在書架B的第",B.get(a),"本")
else:
	print("查無此書籍")
