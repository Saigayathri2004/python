# Initialize an empty dictionary for students
student = {}

# Prompt the user to enter the number of students
n = int(input("Enter the number of students: "))

# Loop through n times to get student details
for i in range(n):
    # Prompt the user to enter the name, age, and grade
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grade = input("Enter the student's grade: ")

    # Add the name, age, and grade to the dictionary
    student[name] = (age, grade)

# Print the student dictionary
print("Student List:", student)