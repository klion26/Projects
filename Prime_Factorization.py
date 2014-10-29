###########################################
# Author: klion26
# Date: 2014/10/29
# Problem: Prime Factorization
###########################################

# Test the input n is a prime number or not
def isPrime(n):
    if n<2: # n is less than 2
        return False
    elif n == 2: # n equals to 2
        return True
    if n%2 == 0: # n is even number
        return False
    # test all odd numbers between 3 and sqrt(n) 
    for i in range(3, (int)(n ** 0.5) + 1, 2):
        if n%i == 0: # if i divids n, then n isn't a prime number
            return False
    return True # n is a prime number

# get all Prime factors of n, and return it
def priFactor(n):
    # vec: all prime numbers less than n
    vec = [2, 3]
    # calulate all prime numbers less than n
    for i in range(5, (int)(n ** 0.5) + 1, 2):
        if isPrime(i):
            vec.append(i)
    # ret: all prime factors of n
    ret = []
    for i in vec:
        if n%i == 0:
            ret.append(i)
    return ret
# input a number
n = (int)(raw_input("input a number:"))
# calculate the prime factors of n
ans = priFactor(n)
# print the answer
for i in ans:
    print i
