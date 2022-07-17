'''
   CS 5001 Homework 3 Programming #2
   Fall 2021
   Shasha Wang
   Oct 6th,2021

   Test case # 1:
   investment_value: 1000
   interest_rate:.5
   expected num_of_years:2

   Test case # 2:
   investment_value: 0
   interest_rate:0
   expected num_of_years: 0

   Test case # 3:
   investment_value: 500
   interest_rate:.3
   expected num_of_years: 3

   Test case # 4:
   investment_value: 8000
   interest_rate:.09
   expected num_of_years: 8

   Test case # 5:
   investment_value: 100
   interest_rate:1
   expected num_of_years: 1

'''


def investment_double(investment_value, interest_rate):
    current_value = investment_value
    number_of_years = 0
    while current_value < 2 * investment_value:
        # update the acccumulated current_value
        current_value = current_value * (1 + interest_rate)
        number_of_years += 1
    return number_of_years


def main():
    investment_value = eval(input("Please enter the investment value:"))
    interest_rate = eval(input("The interest rate is:"))
    result = investment_double(investment_value, interest_rate)
    print(f"It takes {result} years to double the investment.")


main()
