def is_leap_year(year):
  """Checks if a given year is a leap year.

  Args:
      year: An integer representing the year to be checked.

  Returns:
      True if the year is a leap year, False otherwise.
  """

  # Check for divisibility by 4
  if year % 4 == 0:
    # If the year is divisible by 400, it's a leap year
    if year % 400 == 0:
      return True
    # If the year is divisible by 4 but not by 400, it's not a leap year
    elif year % 100 == 0:
      return False
    # Otherwise, it's a leap year
    else:
      return True
  # If the year is not divisible by 4, it's not a leap year
  else:
    return False

# Example usage
year = int(input("Enter a year: "))
if is_leap_year(year):
  print(year, "is a leap year.")
else:
  print(year, "is not a leap year.")
