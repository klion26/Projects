###########################################
# Author: klion26
# Date: 2014/11/08
# Problem: Number_Names
###########################################

def nameNumber(n):
    while n:
        if n>1000:
            t = n/1000
            n = n%1000
            print "%d thound " % (t),
        elif n>100:
            t = n/100
            n = n%100
            print "%d hundred " % (t),
        else:
            print "%d" % (n)
            n /= 10

if __name__ == "__main__":
    n = input("input a number: ")
    nameNumber(n)
