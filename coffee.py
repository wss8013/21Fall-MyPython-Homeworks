'''
   CS 5001 Homework 2 Programming #1
   Fall 2021
   Shasha Wang
   Sep 27th,2021

   Test case # 1:
   coffee weight = 1 pound:
   total cost = 12.86

   Test case # 2:
   coffee weight = 0.5 pound:
   total cost = 7.18

   Test case # 3:
   coffee weight = 7 pound:
   total cost = 81.02

   Test case # 4:
   coffee weight = 100 pound:
   total cost = 1137.5

   Test case # 5:
   coffee weight = 0.1 pound:
   total cost = 2.636
'''
# Assign constant vatiables
FIXED_COST = 1.5
COFFEE_PER_POUND = 10.50
SHIPPING_PER_POUND = 0.86


def coffee_cost(coffee_weight):
    # Calculate coffee cost
    coffee_cost = coffee_weight * COFFEE_PER_POUND
    # Calculate shipping cost
    shipping_cost = coffee_weight * SHIPPING_PER_POUND
    total_cost = coffee_cost + shipping_cost + FIXED_COST
    return total_cost


def main():
    coffee_weight = float(input("Enter how much coffee you want to purchase:\n"))
    print(f"You total cost will be :", coffee_cost(coffee_weight))


main()
