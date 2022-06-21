a = input("請選擇主餐及升級的套餐:")
b = input("是否升級成大杯飲料:")
c = input("是否換成大薯:")
m = 0
if a == "1A":
	m+=127
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
elif a == "1B":
	m+=140
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
elif a == "2A":
	m+=117
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
elif a == "2B":
	m+=130
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
elif a == "3A":
	m+=137
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
elif a == "3B":
	m+=150
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
elif a == "4A":
	m+=99
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
elif a == "4B":
	m+=112
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
elif a == "5A":
	m+=115
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
elif a == "5B":
	m+=128
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
	