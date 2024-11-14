input_string = input("Enter a string: ")

# Extract the first character of the string
first_char = input_string[0]

# Replace all occurrences of the first character in the rest of the string with '$'
modified_string = first_char + input_string[1:].replace(first_char, '$')

# Print the modified string
print("Modified string:", modified_string)