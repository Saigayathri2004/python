l=int(input("enter the length of a rectangle:"))
b=int(input("enter the breadth of a rectangle:"))
s=int(input("enter the side of a square:"))
area=lambda l,b:l*b
perimeter=lambda l,b:2*(l+b)
print("Area of a rectangle :",area(l,b))
print("Perimeter of a rectangle :",perimeter(l,b))
area=lambda s:s*s
perimeter=lambda s:4*s
print("Area of a square :",area(s))
print("Perimeter of a square :",perimeter(s))