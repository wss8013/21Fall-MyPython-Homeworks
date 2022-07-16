'''
   CS 5001 Homework 1 Programming #1
   Fall 2021
   Shasha Wang
   Sep 18th,2021

   Test case #1:
   10k race, 1 hour and 1 minute:
   6.21 miles, 9.49pace, 6.11 MPH

   Test case #2:
   20k race, 3 hour and 18 minute:
   12.42 miles, 15.56 pace, 3.76 MPH

   Test case #3:
   1k race, 0 hour and 5 minute:
   1 miles, 8.03 pace, 7.45 MPH

   Test case #4:
    0 race, 1 hour and  0 minute:
    program crushed with errors
    "ZeroDivisionError: float division by zero"

   Test case #5:
    -10 race,  2 hour and  0 minute:
    -6.21 miles, -20.40 pace,  -3.11 MPH
    Negative input leads to meaningless output
'''
import math


MILE_KILO_FACTOR = 1.61    # MILE_KILO_FACTOR is a constant variable


def main():
    # ask user for how many kilometers
    num_kilo_prompt = input("How many kilometers did you run?\n")
    # convert input from a string to a float number
    num_kilo = float(num_kilo_prompt)
    # ask user for how many hours
    num_hours_prompt = input("How many hours did it take you?\n")
    # convert input from a string to an integer
    num_hours = int(num_hours_prompt)
    # ask user for how many minutes
    num_mins_prompt = input("How many minutes?\n")
    # convert input from a string to an integer
    num_mins = int(num_mins_prompt)
    # convert kilo to mile
    num_miles = num_kilo / MILE_KILO_FACTOR
    # convert total time spend into seconds
    total_seconds = 3600 * num_hours + 60 * num_mins
    # calculate how many miles you run per second
    mile_per_second = num_miles/total_seconds
    # convert mile per second to mile per hour
    mile_per_hour = 3600 * mile_per_second
    # calculate the pace
    pace_per_second = total_seconds/num_miles
    # run down the calculation results of minutes to the nearest integer
    minutes = math.floor(pace_per_second / 60)
    # run down the calculation results of seconds to the nearest integer
    seconds = math.floor(pace_per_second % 60)
    # Print out the results and round off to two decimal places
    print("You ran {} miles".format(round(num_miles, 2)))
    # print out the result
    print("Your pace:", minutes, "min", seconds, "sec per mile")
    # Print out the results and round off to two decimal place
    print("Your MPH: {}". format(round(mile_per_hour, 2)))


main()
