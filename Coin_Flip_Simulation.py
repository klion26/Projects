###########################################
# Author: klion26
# Date: 2014/11/08
# Problem: Coin_Flip_Simulation
###########################################
from random import randint

# simulate the coin flip
def coinFlip(n):
    l = [0, 0] # l[0]-->head l[1]-->tail
    while n:
        a = randint(0, 1) # generate a random number
        l[a] = l[a]+1  # update the answer
        n -= 1 # update the flip number
    return l

if __name__ == "__main__":
    n = input("simulation times: ")
    print coinFlip(n)
