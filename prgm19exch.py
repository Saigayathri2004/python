input_string = input("Enter a string: ")

# Store the first character in 'start' and the last character in 'end'
start = input_string[0]
end = input_string[-1]

# Get the middle part of the string (excluding the first and last characters)
middle = input_string[1:-1]

# Form the new string by swapping the first and last characters
new_string = end + middle + start

# Print the modified string
print("Modified string:", new_string)