###########################################
# Author: klion26
# Date: 2014/11/04
# Problem: Binary_to_Decimal_and_Back_Converter
###########################################

# convert binary to decimal, binary number stored in list l, return the decimal number
def B2D(l):
    # get the length of l
    length = len(l)
    base = 2
    ret = 0
    #print length
    for i in range(0, length):
        ret = ret * base + l[i]
        print ret
    return ret
# convert decimal number to binary
def D2B(n):
    v = []
    while n > 0:
        v.append(n%2)
        n /= 2
    return v[::-1]

print B2D(D2B(157))
