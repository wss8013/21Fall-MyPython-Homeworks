'''
   CS 5001 Homework 4 Programming #1
   Fall 2021
   Shasha Wang
   Oct 11th,2021

   Test case # 1:
   input:"random access memory"
   output: "RAM"

   Test case # 2:
   input:"Welcome to Northeastern University"
   output: "WTNU"

   Test case # 3:
   input:"by the way"
   output: "BTW"

   Test case # 4:
   input:"as soon as possible"
   output: "ASAP"

   Test case # 5:
   input:"Here is my number"
   output: "HIMN"
'''


def acronym(a_phrase):
    acronym = ''
    for i in range(len(a_phrase)):
        if i == 0:
            acronym = a_phrase[0].upper()
        if a_phrase[i].isspace():
            acronym += a_phrase[i+1].upper()
    return acronym


def main():
    a_phrase = input('Please type a phrase:\n')
    print(acronym(a_phrase))

main()
