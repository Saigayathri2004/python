def power(base, exponent):
    # Base case: exponent is 0, return 1
    if exponent == 0:
        return 1
    # Base case: exponent is 1, return base
    elif exponent == 1:
        return base
    else:
        # Recursive case: exponent is greater than 1
        return base * power(base, exponent - 1)

# Taking input from the user
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Calling the power function and printing the result
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")