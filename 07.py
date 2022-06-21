a=int(input("輸入月租費型式:"))
b=int(input("輸入通話時間:"))
if a == 186:
	if b<186/0.09:
		print("通話費為:",a)
	elif b>186/0.09 and b<=(186/0.09)*2:
		print("通話費為:",round(b*0.09*0.9,0))
	else:
		print("通話費為:",round(b*0.09*0.8,0) )
elif a == 386:
	if b<386/0.08:
		print("通話費為:",a)
	elif b>386/0.08 and b<=(386/0.08)*2:
		print("通話費為:",round(b*0.08*0.8,0))
	else:
		print("通話費為:",round(b*0.08*0.7,0) )
elif a == 586:
	if b<586/0.07:
		print("通話費為:",a)
	elif b>586/0.07 and b<=(586/0.07)*2:
		print("通話費為:",round(b*0.07*0.7,0))
	else:
		print("通話費為:",round(b*0.07*0.6,0) )
elif a == 986:
	if b<986/0.06:
		print("通話費為:",a)
	elif b>986/0.06 and b<=(986/0.06)*2:
		print("通話費為:",round(b*0.06*0.6,0))
	else:
		print("通話費為:",round(b*0.06*0.5,0) )


