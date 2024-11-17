student={}
ls={}
print("////////////////////////////")
n=int(input("Enter the number of students:"))
for i in range(0,n):
		print("////////////////////////////")
		Name=input("enter the name of the student:")
		Age=input("enter the age of the student:")
		Grade=input("enter the grade of the student:")
		student[Name]=[Age,Grade]
print("////////////////////////////")
print(student)