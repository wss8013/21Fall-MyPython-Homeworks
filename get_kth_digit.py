'''
CS 5001 Homework 2 Programming #4
   Fall 2021
   Shasha Wang
   Sep 27th,2021

   Test case # 1:
   (n,k)=(789,0)
   expect output:9

   Test case # 2:
   (n,k)=(1234,5)
   expect output:0

   Test case # 3:
   (n,k)=(0,0)
   expect output:0

   Test case # 4:
   (n,k)=(-98,1)
   expect output:9

   Test case # 5:
   (n,k)=(-1234567,11)
   expect output:0
'''


def get_kth_digit(n, k):
    # convert negative n to positive by times -1
    if n < 0:
        n = -1 * n
    while n >= 0 and k >= 0:
        # get the 0th digit of n
        x = n % 10
        # move n to the right by 1 digit
        n = n // 10
        # update k value
        k = k-1
    return x


def main():
    n = int(input("Enter a integer:"))
    k = int(input("which digits do you want to know?"))
    print(f"get_kth_digit {n, k} ==", get_kth_digit(n, k))


main()
