'''
   CS 5001 Homework 3 Programming #5 & #6
   Fall 2021
   Shasha Wang
   Oct 6th,2021

   Test case # 1:
   input: 0
   output: 0

   Test case # 2:
   input: 1
   output: 1

   Test case # 3:
   input: 2
   output: 1

   Test case # 4:
   input: 3
   output: 2

   Test case # 5:
   input: 8
   output: 21
'''
# Assign constant variables
ZERO_TH = 0
FIRST = 1


def fibonacci(n):
    # define zeroth fibonacci number as n_2
    n_2 = 0
    n_1 = 1
    n_th_fibonacci_number = 1
    # zeroth fibonacci number is always 0
    if n == 0:
        return ZERO_TH
    # first fibonacci number is always 1
    if n == 1:
        return FIRST
    # calculate n_th fibonacci number when n > 1
    for i in range(2, n+1):
        n_th_fibonacci_number = n_2 + n_1
        # shift n_2 and n_1 to the right by 1
        n_2 = n_1
        n_1 = n_th_fibonacci_number
    return n_th_fibonacci_number


def test_fibonacci():
    result = fibonacci(0)
    print(f"The calculated 0_th fibonacci numer is {result}")
    print(f"The expected 0_th fibonacci numer is 0")
    result = fibonacci(1)
    print(f"The calculated first fibonacci numer is {result}")
    print(f"The expected first fibonacci numer is 1")
    result = fibonacci(2)
    print(f"The calculated second fibonacci numer is {result}")
    print(f"The expected second fibonacci numer is 1")
    result = fibonacci(3)
    print(f"The calculated third fibonacci numer is {result}")
    print(f"The expected third fibonacci numer is 2")
    result = fibonacci(8)
    print(f"The calculated 8_th fibonacci numer is {result}")
    print(f"The expected 8_th fibonacci numer is 21")


def main():
    test_fibonacci()


main()
