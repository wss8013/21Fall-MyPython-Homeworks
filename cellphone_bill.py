'''
   CS 5001 Homework 2 Programming #5
   Fall 2021
   Shasha Wang
   Sep 27th,2021

   Test case # 1:
   airtime,message = (50,50)
   expect output:16.21

   Test case # 2:
   airtime,message = (0,50)
   expect output:16.21

   Test case # 3:
   airtime,message = (100,100)
   expect output:37.21

   Test case # 4:
   airtime,message = (0,0)
   expect output:16.21

   Test case # 5:
   airtime,message = (10,10)
   expect output:16.21
'''


BASE = 15
S911_CHARGE = .44
AIRTIME_COST = .25
MESSAGE_COST = .15
TAX_FACTOR = 0.05


# A function to calculate additional airtime cost
def addi_air_cost(airtime):
    if airtime > 50:
        addi_air_cost = (airtime - 50) * AIRTIME_COST
    else:
        addi_air_cost = 0
    return addi_air_cost


# A function to calculate additional message cost
def addi_mesg_cost(message):
    if message > 50:
        addi_mesg_cost = (message - 50) * MESSAGE_COST
    else:
        addi_mesg_cost = 0
    return addi_mesg_cost


def total_bill(airtime, message):
    add_air_cost = addi_air_cost(airtime)
    add_mesg_cost = addi_mesg_cost(message)
    tax = (BASE + S911_CHARGE + add_air_cost + add_mesg_cost) * TAX_FACTOR
    total_bill = BASE + S911_CHARGE + add_air_cost + add_mesg_cost + tax
    # Apply conditions to display additional costs
    if add_air_cost != 0:
        print("Addition air cost is", add_air_cost)
    if add_mesg_cost != 0:
        print("Addition message cost is", add_mesg_cost)
    print("The base charge is:", BASE)
    print("The 911 support charge is:", S911_CHARGE)
    print("Tax cost is", tax)
    print("The total cost is", round(total_bill, 2))


def main():
    airtime = eval(input("Enter the airtime:\n"))
    message = eval(input("Enter the message number:\n"))
    total_bill(airtime, message)


main()
