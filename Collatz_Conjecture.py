###########################################
# Author: klion26
# Date: 2014/11/05
# Problem: Collatz_Conjecture
###########################################
import sys
def Collatz(n):
    # test the range of parameter n
    if n<1:
        print "Invalid number, should bigger than 1"
        sys.exit()
    # init the answer 
    step = 1
    while n > 1:
        if n&1 == 1: # if n is an odd number
            n = 3*n + 1
        else: # n is an even number
            n = n/2
        step = step+1 # update step
    # print the anser
    print "It takes %d steps make n to 1" % (step)

if __name__ == "__main__":
    n = input("Input a number to process: ")
    Collatz(n)
