month = int(input("請輸入出生月:"))
day = int(input("請輸入出生日:"))
if month==1:
	if day < 20:
		print("摩羯座Capricorn")
	else:
		print("水瓶座Aquarius")
elif month==2:
	if day < 19:
		print("水瓶座Aquarius")
	else:
		print("雙魚座Pisces")
elif month==3:
	if day < 21:
		print("雙魚座Pisces")
	else:
		print("白羊座Aries")
elif month==4:
	if day < 21:
		print("白羊座Aries")
	else:
		print("金牛座Taurus")
elif month==5:
	if day < 21:
		print("金牛座Taurus")
	else:
		print("雙子座Gemini")
elif month==6:
	if day < 22:
		print("雙子座Gemini")
	else:
		print("巨蟹座Cancer")
elif month==7:
	if day < 23:
		print("巨蟹座Cancer")
	else:
		print("獅子座Leo")
elif month==8:
	if day < 23:
		print("獅子座Leo")
	else:
		print("處女座Virgo")
elif month==9:
	if day < 23:
		print("處女座Virgo")
	else:
		print("天秤座Libra")
elif month==10:
	if day < 23:
		print("天秤座Libra")
	else:
		print("天蠍座Scorpio")
elif month==11:
	if day < 22:
		print("天蠍座Scorpio")
	else:
		print("射手座Sagittarius")
else:
	if day < 22:
		print("射手座Sagittarius")
	else:
		print("魔羯座Capricorn")