'''
   CS 5001 Homework 3 Programming #3
   Fall 2021
   Shasha Wang
   Oct 6th,2021

   Test case # 1:
   interest_rate:0
   expected output: 95000

   Test case # 2:
   interest_rate:.01
   expected output: 104054

   Test case # 3:
   interest_rate:.05
   expected output: 152695

   Test case # 4:
   interest_rate:1
   expected output: 2621435000

   Test case # 5:
   interest_rate:.03
   expected output: 125584

'''
# assign constant variable
ADD_PER_YEAR = 5000


def college_savings(interest_rate):
    savings = 5000
    for i in range(0, 18):
        # update the accumulated savings each year
        savings = savings * (1 + interest_rate) + ADD_PER_YEAR
    return savings


def main():
    interest_rate = eval(input("Please enter the interest rate:"))
    result = college_savings(interest_rate)
    print(f"Emma's college savings fund is {result} when she turns 18.")

main()
