###########################################
# Author: klion26
# Date: 2014/11/08
# Problem: Complex_Number_Algebra
###########################################

# complex addition
# complex number is stored in list [x,y]->x+yi
def add(a, b):
    c = []
    c.append(a[0]+b[0])
    c.append(a[1]+b[1])
    return c
# complex multiplication
def mul(a, b):
    c = []
    c.append(a[0]*b[0] - a[1]*b[1])
    c.append(a[0]*b[1] + a[1]*b[0])
    return c

def neg(a):
    c = [-i for i in a]
    return c

# print a complex number
def comPrint(a):
    print "%d + %di" % (a[0], a[1])
    
if __name__ == "__main__":
    comPrint(add([1,2], [3,4]))
    print mul([2,6], [3,7])
    print neg([5,8])
