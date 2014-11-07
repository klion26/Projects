###########################################
# Author: klion26
# Date: 2014/11/07
# Problem: Unit_Converter
###########################################

#temperature convertor
def tempCon(op, val):
    if op==1: # C->F
        return (1.0*val*9/5)+32
    else: # F->C
        return (val-32)*5.0/9

# meter convertor
def meterCon(op, val):
    if op==1: # cm->m
        return val/100.0
    elif op==2 : # dm->m
        return val/10.0
    elif op==3 : # m->cm
        return val*100
    else:  #m->dm
        return val*10

# volume convertor
def volCon(op, val):
    if op==1: # ml->l
        return val/1000.0
    else: #l->ml
        return val*1000

if __name__ == "__main__":
    n = input("which convertor do you want to use:\n1. Temperature\n2. Meter\n3. Volume\n")
    if n==1:
        op = input("do you want to convert from\n 1).C to F\n 2). F to C\n")
        val = input("please input the value you want to conver: ")
        print tempCon(op, val)
    elif n==2:
        op = input("do you want to convert from\n 1). cm->m\n 2). dm->m\n 3). m->cm\n 4). m->dm\n")
        val = input("please input the value you want to conver: ")
        print meterCon(op, val)
    else:
        op = input("do you want to convert from\n 1). ml->l\n 2). l->ml\n")
        val = input("please input the value you want to conver: ")
        print meterCon(op, val)
