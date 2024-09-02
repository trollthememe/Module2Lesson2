# Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

leap_year = int(input("Enter a year: "))
# Used this formula for divisiability: A is divisible by B if A % B == 0. Using f string for easier reading of code.

if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print(f"{leap_year} is a leap year")
        else:                                           # 3 else statements for 3 if statements
            print(f"{leap_year} is not a leap year")
    else:
        print(f"{leap_year} is a leap year")
else:
    print(f"{leap_year} is not a leap year")