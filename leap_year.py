'''
   CS 5001 Homework 2 Programming #3
   Fall 2021
   Shasha Wang
   Sep 27th,2021

   Test case # 1:
   100
   is not Leap year

   Test case # 2:
   1800
   is not leap year

   Test case # 3:
   23
   is not leap year

   Test case # 4:
   1600
   is leap year

   Test case # 5:
   2016
   is leap year
'''


def is_leap_year(year):
    # A year is not a century year and divisible by 4
    if (year % 100 != 0 and year % 4 == 0):
        isleap = True
    # A year is century year and divisible by 400
    elif (year % 100 == 0 and year % 400 == 0):
        isleap = True
    else:
        isleap = False
    return isleap


def main():
    year = int(input("Enter a year:\n"))
    if is_leap_year(year):
        print(year, "is leap year!")
    else:
        print(year, "is not leap year!")


main()
