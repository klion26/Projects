###########################################
# Author: klion26
# Date: 2014/11/11
# Problem: Sieve_of_Eratosthenes
###########################################

# Sieve of Eratosthenes
def sieveEratosthenes(n):
    # get the list of [2,3 ... n]
    # use range instead of xrange, because xrange is a generator,
    # and range will return a list
    l = range(2, n+1)
    # index of the current prime number
    i = 0
    # process all the number
    while i < len(l):
        # remove all l[i]'s multiply from list l
        j = i+1
        while j < len(l):
            if l[j]%l[i] == 0:
                l.pop(j)  # remove this number if it's l[i]'s multiply
            j += 1
        i += 1
    #return all the prime numbers less than n
    return l

# sieve 2
def sieve(n):
    is_prime = [False]*2 + [True]*(n-1)
    for i in xrange(int(n**0.5 + 1.5)): # stop at sqrt(n), add 1.5 because we need stop at (n**0.5+1.5-1)
        if is_prime[i]:
            for j in xrange(i*i, n+1, i):
                is_prime[j] = False
    return [i for i,prime in enumerate(is_prime) if prime]
# test 
print sieveEratosthenes(30)
print sieve(30)
        
