###########################################
# Author: klion26
# Date: 2014/11/03
# Problem: Change Return Program
###########################################

# calculate the changes of *cost* and *given*
def calChange(cost, given):
    # return the change list
    change = []
    # figure out the money left
    given -= cost
    # a list of quarters, dimes, nickels and pennies
    fvalue = [25, 10, 5, 1]
    idx = 0

    # while there still has money
    while given > 0:
        if given > fvalue[idx]: # use the current value 
            change.append(given/fvalue[idx]) #calculate the number of value fvalue[idx]
            given %= fvalue[idx] #update the money we still have
        else:
            change.append(0)  # use use the current value
        idx += 1 # update the index
    return change # return the answer

# wrapper
def main():
    # input the cost and given money
    c = input("input the cost: ")
    g = input("input the given money: ")
    # call calChange() to calculate the answer
    t = calChange(c, g)
    # print all the answer
    for i in t:
        print i,

if __name__ == "__main__":
    main()
