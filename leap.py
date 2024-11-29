def find_next_leap_year(year):
    """Finds the next leap year."""
    while not is_leap_year(year):
        year += 1
    return year

def is_leap_year(year):
    """Checks if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main():
    print("Leap Year Finder")
    print("------------------")

    user_input = input("Enter a year (leave blank for current year): ")

    if user_input:
        year = int(user_input)
    else:
        from datetime import date
        year = date.today().year

    next_leap_year = find_next_leap_year(year)

    print(f"The next leap year from {year} is {next_leap_year}")

if __name__ == "__main__":
    main()
