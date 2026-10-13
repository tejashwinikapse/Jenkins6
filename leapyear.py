def leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


year = int(input("Enter a year: "))

result = leap_year(year)

print("Year:", year)
print("Leap Year:", result)