student=[]
n=int(input("Enter the no of students:"))
total=int(input("Enter the total no of classes:"))
for i in range(n):
     name=input("Enter the name of the student:")
     no=int(input("Enter the no of classes present:"))
     percent=(no/total)*100
     student.append([percent,name])
student.sort()
print(student)