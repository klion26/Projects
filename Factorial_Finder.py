###########################################
# Author: klion26
# Date: 2014/11/05
# Problem: Factorial_Finder
###########################################

# calculate n! with loops
def factorialLoop(n):
    ret = 1
    i = 1
    while i<=n:
        ret *= i
        i += 1
    return ret

# calculate n! with recursion
def factorialRec(n):
    if n < 2:
        return 1
    return n * factorialRec(n-1)

# main wrapper, and test with 12!
if __name__ == "__main__":
    print factorialLoop(12)
    print factorialRec(12)
