def filter_positive_numbers(input_list):
    """Filters positive numbers from the input list."""
    positive_list = [num for num in input_list if num > 0]
    return positive_list

def main():
    try:
        input_list = list(map(int, input("Enter numbers separated by space: ").split()))
        positive_list = filter_positive_numbers(input_list)
        
        print("Input List:", input_list)
        print("Positive List:", positive_list)
    
    except ValueError:
        print("Error: Please enter only valid integers separated by spaces.")

if __name__ == "__main__":
    main()

