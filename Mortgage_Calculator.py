###########################################
# Author: klion26
# Date: 2014/11/01
# Problem: Mortgage Calculator
###########################################

# monthly payment: (����*������*(1+������)^��������) / ((1+������)^�������� -1)
# S = a/(1+r) + a/(1+r)^2 + ... + a/(1+r)^n
def Mortgage(c, x, n):
    return c * x * ((1+x)**n) / (((1+x)**n)-1)

print Mortgage(100, 0.04, 5)
