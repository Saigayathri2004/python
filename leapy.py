def main():
	print("leap years....\n ----------------")
	start=int(input("enter the year to start with search : "))
	st=int(input("enter the year to end the search : "))
	for i in range(start,st+1):
		if(i%4==0 && i%100!=0):
			print(i)
	print("this are the leap years") 			
