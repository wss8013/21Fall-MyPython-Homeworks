'''
   CS 5001 Homework 1 Programming #3
   Fall 2021
   Shasha Wang
   Sep 18th,2021

   Test case #1:
   1 wheels, 3 frames, 55 links
   bike possible: 0
   parts left: 1 wheel, 3 frames, 55 links

   Test case #2:
   10 wheels, 1 frames, 200 links
   bike possible: 1
   parts left: 8 wheel, 0 frames, 150 links

   Test case #3:
   4 wheels, 2 frames, 100 links
   bike possible: 2
   parts left: 0 wheel, 0 frames, 0 links

   Test case #4:
   0 wheels, 0 frames, 0 links
   bike possible: 0
   parts left: 0 wheel, 0 frames, 0 links

   Test case #5:
   100 wheels, 100 frames, 100 links
   bike possible: 2
   parts left:96 wheel, 98 frames, 0 links
'''


def main():
    # ask user for how many wheels
    num_wheels_prompt = input("How many wheels do you have?\n")
    # convert input to integer
    num_wheels = int(num_wheels_prompt)
    # ask user for how many frames
    num_frames_prompt = input("How many frames do you have?\n")
    # convert input to integer
    num_frames = int(num_frames_prompt)
    # ask user for how many links
    num_links_prompt = input("How many links do you have?\n")
    # convert input to integer
    num_links = int(num_links_prompt)
    # use build in minimum function to get the minimum bike number
    bikes_possible = min(num_wheels//2, num_frames//1, num_links//50)
    # calculate the number of wheels left
    left_wheels = num_wheels-2 * bikes_possible
    # calculate the number of frames left
    left_frames = num_frames-1 * bikes_possible
    # calculate the number of links left
    left_links = num_links-50 * bikes_possible
    # print out the results
    print("All totalled up, you've got", bikes_possible, "bikes coming\n",
          "I will keeping the leftovers for myself\n", "Leftover:\n",
          left_wheels, "wheels\n", left_frames, "frams\n", left_links, "links")


main()
