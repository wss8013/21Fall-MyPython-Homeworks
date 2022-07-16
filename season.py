'''
   CS 5001 Homework 2 Programming #6
   Fall 2021
   Shasha Wang
   Sep 27th,2021

   Test case # 1:
   month: January
   day:3
   Expected output: winter

   Test case # 2:
   month: ABC
   day:3
   Expected output: Error

   Test case # 3:
   month: March
   day:20
   Expected output: spring

   Test case # 4:
   month: December
   day:1
   Expected output: fall

   Test case # 5:
   month: June
   day:21
   Expected output: summer
'''

JAN = "January"
FEB = "February"
MAR = "March"
APR = "April"
MAY = "May"
JUN = "June"
JUL = "Jul"
AUG = "August"
SEP = "Septemner"
OCT = "October"
NOV = "November"
DEC = "December"


def convert_month_string_to_number(month):
    # convert the month from a string to a integer
    # in order to simplify the range comparison
    month_number = 0
    if month == JAN:
        month_number = 1
    elif month == FEB:
        month_number = 2
    elif month == MAR:
        month_number = 3
    elif month == APR:
        month_number = 4
    elif month == MAY:
        month_number = 5
    elif month == JUN:
        month_number = 6
    elif month == JUL:
        month_number = 7
    elif month == AUG:
        month_number = 8
    elif month == SEP:
        month_number = 9
    elif month == OCT:
        month_number = 10
    elif month == NOV:
        month_number = 11
    elif month == DEC:
        month_number = 12
    return month_number


def season(month, day):
    # convert string month to an integer
    month_number = convert_month_string_to_number(month)
    # if month_number is 0 then the month is not a valid input
    # return an error string
    if(month_number == 0):
        return "Error"
    # return winter when the date falls into one of the following condition
    # 1. month is less than 3 (earlier than March)
    # 2. month is 3 and day less than 20 (earlier than March 20 )
    # 3. month is 12 and day is greater than or equal to 21 (Later than Dec 20)
    if ((month_number < 3) or
            (month_number == 12 and day >= 21) or
            (month_number == 3 and day < 20)):
        return "winter"
    # return spring when the date falls into one of the following condition
    # 1. month is in bwteen 3 and 6  (later than March earlier than June )
    # 2. month is 3 and day greater than or equal to 20 (later than March 20 )
    # 3. month is 6 and day is less to 21 (earlier than Jun 21)
    elif ((month_number == 3 and day >= 20) or
            (month_number > 3 and month_number < 6) or
            (month_number == 6 and day < 21)):
        return "spring"
    # return summer when the date falls into one of the following condition
    # 1. month is in bwteen 6 and 9  (later than June earlier than Sep )
    # 2. month is 6 and day greater than or equal to 21 (later than June 21 )
    # 3. month is 9 and day is less than 22 (earlier than Sep 22)
    elif ((month_number == 6 and day >= 21) or
            (month_number > 6 and month_number < 9) or
            (month_number == 9 and day < 22)):
        return "summer"
    # return fall when the date falls into one of the following condition
    # 1. month is in bwteen 9 and 12  (later than Sep earlier than Dec )
    # 2. month is 9 and day greater than or equal to 22 (later than Sep 22 )
    # 3. month is 12 and day is less than 21 (earlier than Dec 21)
    elif ((month_number == 9 and day >= 22) or
            (month_number > 9 and month_number < 12) or
            (month_number == 12 and day < 21)):
        return "fall"
    return "Error"


def main():
    month = input("Give me the month: \n")
    day = int(input("Give me the day: \n"))
    m_season = season(month, day)
    if (m_season == "Error"):
        print("Something went wrong please re-run the program")
    else:
        print(f"The season is {m_season}")
main()
