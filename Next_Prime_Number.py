###########################################
# Author: klion26
# Date: 2014/10/30
# Problem: Next Prime Number
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

# Generate the next prime begin with n(include)
def genNextPrime(n):
    while True:
        if isPrime(n):
            break;
        else:
            n += 1
    return n

# Warp of main function
def main():
    num = 2

    while True:
        # Get the user input
        ans = raw_input("Would you like to see the next prime? (Y/N) ")

        # Test the input
        if ans.lower().startswith('y'):
            print(num)
            num = genNextPrime(num+1)
        else:
            break

if __name__ == '__main__':
    main()
