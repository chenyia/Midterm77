All=set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
E=set(['John','Mary','Fiona','Claire','Ben','Bill'])
M=set(['Mary','Fiona','Claire','Eva','Ben'])
print("數學與英文都及格",E&M)
print("數學不及格",All^M)
print("英文及格且數學不及格",E&(All^M))
