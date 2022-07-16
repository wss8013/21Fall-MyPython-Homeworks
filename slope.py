'''
   CS 5001 Homework 2 Programming #2
   Fall 2021
   Shasha Wang
   Sep 27th,2021

   Test case # 1:
   x1 = 0
   x2 = 0
   y1 = 0
   y2 = 0
   output: error message

   Test case # 2:
   x1 = 1
   x2 = 2
   y1 = 3
   y2 = 4
   output: 1

   Test case # 3:
   x1 = -10
   x2 = -20
   y1 = -30
   y2 = -40
   output: 1

   Test case # 4:
   x1 = 15
   x2 = 4
   y1 = 60
   y2 = 16
   output: 4

   Test case # 5:
   x1 = -1
   x2 = -3
   y1 = 6
   y2 = 9
   output: -1.5
'''


def cal_slope(x1, y1, x2, y2):
    slope = 0
    error_message = ""
    # check whether x1 and x2 are equal, if so, return error message
    if x1 != x2:
        slope = (y2 - y1)/(x2 - x1)
    else:
        error_message = "Error: slope does not exist!"
    return slope or error_message


def main():
    # take user inputs
    x1 = float(input("Enter x1:"))
    x2 = float(input("Enter x2:"))
    y1 = float(input("Enter y1:"))
    y2 = float(input("Enter y2:"))
    # call cal_slope to calculate the slope value
    result = cal_slope(x1, y1, x2, y2)
    # print out the result based on the return value
    if type(result) == str:
        print(result)
    else:
        print("The slope of the two points is", result)


main()
