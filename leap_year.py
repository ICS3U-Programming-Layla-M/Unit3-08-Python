#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May, 12, 2021
# This program asks the user to input a year
# and displays if it's a leap year or not


def main():
    # check for invalid input
    try:
        year = int(input("Enter a year: "))
    except ValueError:
        # error message
        print("Please enter a valid year.")
    else:
        # check that year is not a negative number
        if (year < 0):
            print("Please enter a valid year.")
        # displays if the year is a leap year or not
        else:
            if (year % 4) == 0:
                if (year % 100) == 0:
                    if (year % 400) == 0:
                        print("{} is a leap year.". format(year))
                    else:
                        print("{} is not a leap year.". format(year))
                else:
                    print("{} is a leap year.". format(year))
            else:
                print("{} is not a leap year.". format(year))


if __name__ == "__main__":
    main()
