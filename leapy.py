def is_leap_year(year):
    """
    Function to check if a year is a leap year.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def display_leap_years(start_year, end_year):
    """
    Function to display all leap years between two given years.
    """
    if start_year > end_year:
        start_year, end_year = end_year, start_year
    
    print(f"Leap years between {start_year} and {end_year}:")
    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            print(year, end=" ")
    print()

# Input
try:
    start_year = int(input("Enter the starting year: "))
    end_year = int(input("Enter the ending year: "))
    display_leap_years(start_year, end_year)
except ValueError:
    print("Please enter valid integers for the years.")
) 			
