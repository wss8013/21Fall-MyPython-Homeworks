'''
   CS 5001 Homework 3 Programming #4
   Fall 2021
   Shasha Wang
   Oct 6th,2021
'''
MONTHLY_PAYMENT = 50
MONTHLY_INTEREST_RATE = 0.015


def main():
    debt = 1000
    num_month = 0
    total_interest = 0
    while debt > 0:
        # calculate the current interest of the month based on the current debt
        interest = debt * MONTHLY_INTEREST_RATE
        # subtract the interest from the monthly payment 
        remaining_payment = MONTHLY_PAYMENT - interest
        # apply what has left to pay back the debt 
        debt = debt - remaining_payment
        # count the number of month 
        num_month += 1
        # sum up the total interest
        total_interest += interest
    print(f" It takes {num_month} month to pay off the loan.\n")
    print(f" The total amount of interest of the loan is {total_interest}")

main()
