"""
Pi = SUM k=0 to infinity 16^-k [ 4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6)]
"""
import math
from decimal import Decimal as D
from decimal import getcontext
def calDigit(digit):
    return D(math.pow(16, -digit)) * (D(4.0 / (8*k + 1)) - D(2.0/(8*k+4)) - D(1.0/(8*k+5)) - D(1.0/(8*k+6)))

getcontext().prec = 400
PI=0
for k in range(50):
    PI += calDigit(k)

print "PI>>>>> %.*f" % (10, PI)
