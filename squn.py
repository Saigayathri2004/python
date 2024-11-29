def calculate_squares(n):
    """Calculates squares of 'n' numbers."""
    squares = []
    for i in range(1, n+1):
        square = i ** 2
        squares.append(square)
    return squares

def main():
    n = int(input("Enter the value of 'n': "))
    squares = calculate_squares(n)
    print(f"Squares of first {n} numbers:")
    for i, square in enumerate(squares, start=1):
        print(f"{i}^2 = {square}")

if __name__ == "__main__":
    main()
