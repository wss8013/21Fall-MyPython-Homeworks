'''
   CS 5001 Homework 3 Programming #2
   Fall 2021
   Shasha Wang
   Oct 6th,2021

   Test case # 1:
   num_of_years: 1
   interest_rate:.3
   expected output: 6500

   Test case # 2:
   num_of_years: 0
   interest_rate:.5
   expected output: 5000

   Test case # 3:
   num_of_years: 10
   interest_rate:0
   expected output: 5000

   Test case # 4:
   num_of_years: 3
   interest_rate:.09
   expected output: 6475

   Test case # 5:
   num_of_years: 0
   interest_rate:.0
   expected output: 5000
'''


def investment_double(num_of_years, interest_rate):
    investment_value = 5000
    # for each year calculate the accumulated investment value
    for i in range(0, num_of_years):
        investment_value = investment_value * (1 + interest_rate)

    return investment_value


def main():
    num_of_years = int(input("Please enter the number of years:\n"))
    interest_rate = float(input("The annualized interest rate is:\n"))
    result = investment_double(num_of_years, interest_rate)
    print(f'Your investment value is {result}')


main()
