# Define the string
string = "Your example string here"

# Initialize the count variable to 0
count = 0

# Iterate through each character in the string
for char in string:
    # Check if the character is not a space
    if char != ' ':
        count += 1

# Print the result
print("Number of characters (excluding spaces):", count)
