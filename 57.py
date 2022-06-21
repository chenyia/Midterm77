a = list(input("請選擇主餐及升級的套餐:"))
b = input("是否升級成大杯飲料:")
c = input("是否換成大薯:")
m = 0
if a[0] == "1":
	m+=72
	if a[1] =="A":
		m+=55
		if b == "是":
			m+=7
			if c == "是":
				m+=13
			else:
				m=m 
		else:
			m=m
			if c == "是":
				m+=13
			else:
				m=m
	elif a[1] == "B":
		m+=68
		if b == "是":
			m+=7
			if c == "是":
				m+=13
			else:
				m=m 
		else:
			m=m
			if c == "是":
				m+=13
			else:
				m=m
elif a[0] == "2":
	m+=62
	if a[1] =="A":
		m+=55
		if b == "是":
			m+=7
			if c == "是":
				m+=13
			else:
				m=m 
		else:
			m=m
			if c == "是":
				m+=13
			else:
				m=m
	elif a[1] == "B":
		m+=68
		if b == "是":
			m+=7
			if c == "是":
				m+=13
			else:
				m=m 
		else:
			m=m
			if c == "是":
				m+=13
			else:
				m=m
elif a[0] == "3":
	m+=82
	if a[1] =="A":
		m+=55
		if b == "是":
			m+=7
			if c == "是":
				m+=13
			else:
				m=m 
		else:
			m=m
			if c == "是":
				m+=13
			else:
				m=m
	elif a[1] == "B":
		m+=68
		if b == "是":
			m+=7
			if c == "是":
				m+=13
			else:
				m=m 
		else:
			m=m
			if c == "是":
				m+=13
			else:
				m=m
elif a[0] == "4":
	m+=44
	if a[1] =="A":
		m+=55
		if b == "是":
			m+=7
			if c == "是":
				m+=13
			else:
				m=m 
		else:
			m=m
			if c == "是":
				m+=13
			else:
				m=m
	elif a[1] == "B":
		m+=68
		if b == "是":
			m+=7
			if c == "是":
				m+=13
			else:
				m=m 
		else:
			m=m
			if c == "是":
				m+=13
			else:
				m=m
elif a[0] == "5":
	m+=60
	if a[1] =="A":
		m+=55
		if b == "是":
			m+=7
			if c == "是":
				m+=13
			else:
				m=m 
		else:
			m=m
			if c == "是":
				m+=13
			else:
				m=m
	elif a[1] == "B":
		m+=68
		if b == "是":
			m+=7
			if c == "是":
				m+=13
			else:
				m=m 
		else:
			m=m
			if c == "是":
				m+=13
			else:
				m=m
print("總共為",m,"元")
	