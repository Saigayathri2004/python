def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def power(a,b):
    return a^b
def calculator(num1,operator,num2):
    if operator=="+":
        return add(num1,num2)
    elif operator=="-":
        return substract(num1,num2)
    elif operator=="*":
        return multiply(num1,num2)
    elif operator=="/":
        return division(num1,num2)
    elif operator=="^":
        return power(num1,num2)
    else:
        return "invalid operator"
num1=float(input("enter first number: "))
operator=input("enter an operator(+,-,*,/,^): ")
num2=float(input("enter second number: "))
result=calculator(num1,operator,num2)
print("the result is: ",result)