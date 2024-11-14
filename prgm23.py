# Input the number of names
num_names = int(input("Enter the number of names: "))

# Declare an empty list to store names
names = []

# Input the names and append each to the list
for _ in range(num_names):
    name = input("Enter a name: ")
    names.append(name)

# Sort the list in alphabetical order
names.sort()

# Print the names in alphabetical order
print("Names in alphabetical order:")
for name in names:
    print(name)
