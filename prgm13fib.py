def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter a number of terms"))
print("fibonacci series.....")
for i in range(n):
    print(fibonacci(i))
    result=fibonacci(n-1)