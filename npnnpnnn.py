def compute_expression(n):
    # Compute the value of n + nn + nnn
    nn = int(str(n) * 2)  # n concatenated with n to form nn
    nnn = int(str(n) * 3)  # n concatenated with n and n to form nnn
    result = n + nn + nnn
    return result

# Example usage:
n = int(input("Enter an integer: "))
result = compute_expression(n)
print("Result of n + nn + nnn is:", result)

