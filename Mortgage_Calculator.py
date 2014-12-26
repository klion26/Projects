###########################################
# Author: klion26
# Date: 2014/11/01
# Problem: Mortgage Calculator
###########################################

# monthly payment: (本金*月利率*(1+月利率)^还款期数) / ((1+月利率)^还款期数 -1)
# S = a/(1+r) + a/(1+r)^2 + ... + a/(1+r)^n
def Mortgage(c, x, n):
    return c * x * ((1+x)**n) / (((1+x)**n)-1)

print Mortgage(100, 0.04, 5)
