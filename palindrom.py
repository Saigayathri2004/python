def is_palindrome(n):
    n_str=str(n)
    n_rev=n_str[::-1]
    if n_str==n_rev:
                 return True
    else:
        return False
n=input("enter an input: ")
result=is_palindrome(n)
if result:
        print("the input is a palindrome")
else:
        print("the input is not palindrome")