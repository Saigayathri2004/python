details={}
print("/////////////////////")
n=int(input("enter the limit of the details:"))
for i in range(n):
		print("///////////////////")
		name=input("enter the name :")
		grade=input("enter the grade:")
		mark=input("enter the marks:")
		details[name]=[grade,mark]
ls=list(details.items())
r=list(details.items())
ls.sort()
print("sorting in ascending order:",ls)
r.sort(reverse=True)
print("sorting in descending order:",r)
a=dict(ls)
b=dict(r)
print ("Print in dictionary:",a) 
print("print in dictionary:",b)