###########################################
# Author: klion26
# Date: 2014/11/07
# Problem: Tax_Calculator
###########################################

def taxCal(val, tax):
    return val*(1+tax)

if __name__ == "__main__":
    v = input("Input the cost: ")
    tax = input("input the tax rate(0-100): ")
    print taxCal(v, tax/100.0)
