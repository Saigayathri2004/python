def sum(n):
    s=0
    for i in range (1,n+1):
        s=s+i
    return s
n=int(input("Enter the number:"))
result=sum(n)
print("sum of number is :",result)