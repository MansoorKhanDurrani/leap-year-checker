def check_leap_year(year):
    """Check whether a given year is a leap year.
    
    A year is a leap year if it is divisible by 4,
    except for century years, which must be divisible by 400.
    """
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def get_valid_year():
    """Prompt the user until a valid year is entered."""
    while True:
        try:
            year = int(input("Enter a year: "))
            if year <= 0:
                print("Please enter a positive year.")
                continue
            return year
        except ValueError:
            print("Invalid input. Please enter a numeric year.")


if __name__ == "__main__":
    year = get_valid_year()
    if check_leap_year(year):
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year!")