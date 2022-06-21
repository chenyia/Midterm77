# 作法一

dict1 = {"123":["Tom","DTGD"],"456":["Cat","CSIE"],"789":["Nana","ASIE"],"321":["Lim","DBA"],"654":["Won","FDD"]}
a = input("請輸入欲查詢學號:")
print("學生資料為:",a,dict1.get(a)[0],dict1.get(a)[1])

# 作法二
dict2 = {123:"Tom",456:"Cat",789:"Nana",321:"Lim",654:"Won"}
dict3 = {123:"DTGD",456:"CSIE",789:"ASIE",321:"DBA",654:"FDD"}
a = int(input("請輸入欲查詢學號:"))
print("學生資料為:",a,dict2.get(a),dict3.get(a))

