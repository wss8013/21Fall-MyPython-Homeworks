'''
   CS 5001 Homework 1 Programming #2
   Fall 2021
   Shasha Wang
   Sep 18th,2021

   Test case # 1:
   $4.5:
   4 dollars, 2 quarters, 0 dimes,0 nickels, 0 pennies

   Test case # 2:
   $.2879:
   0 dollars, 1 quarters, 0 dimes,0 nickels, 3 pennies

   Test case # 3:
   $.50:
   0 dollars, 2 quarters, 0 dimes,0 nickels, 0 pennies

   Test case # 4:
   $11.925:
   11 dollars, 3 quarters, 1 dimes, 1 nickels,2 pennies

   Test case # 5:
   -$100:
   -100 dollars, 0 quaeters, 0 dimes,0 nickels, 0 pennies
   Negative input leads to meaningless output
'''

DOLLAR = 1         # DOLLAR is constant variable
QUARTER = .25      # QUARTER is constant variable
DIME = .10         # DIME is constant variable
NICKEL = .05       # NICKEL is constant variable
PENNY = .01        # PENNY is constant variable


def main():
    # Ask user for input with prompt
    change_amount_prompt = input("Enter the change amount\n")
    # convert "string" input to float type
    change_amount = float(change_amount_prompt)
    # calculate number of dollars
    num_dollars = change_amount // DOLLAR
    # calculate number of quarters
    num_quarters = (change_amount - num_dollars * DOLLAR) // QUARTER
    # calculate number of dimes
    num_dimes = (change_amount - num_dollars * DOLLAR -
                 num_quarters * QUARTER) // DIME
    # calculate number of nickels
    num_nickels = (change_amount - num_dollars * DOLLAR -
                   num_quarters * QUARTER - num_dimes * DIME) // NICKEL
    # calculate number of pennies
    num_pennies = (change_amount - num_dollars * DOLLAR -
                   num_quarters * QUARTER - num_dimes * DIME -
                   num_nickels * NICKEL) // PENNY
    # print out the results
    print("That breaks down to...\n", int(num_dollars), "dollars\n",
          int(num_quarters), "quarters\n", int(num_dimes), "dimes\n",
          int(num_nickels), "nickels\n", int(num_pennies), "pennies\n")


main()
