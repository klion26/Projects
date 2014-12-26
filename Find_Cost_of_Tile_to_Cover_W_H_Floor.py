###########################################
# Author: klion26
# Date: 2014/11/01
# Problem: Find Cost of Tile to Cover W*H Floor
###########################################

# calculate the cost of W*H Floor
def calCost(w, h, cost):
    return w*h*cost


w = input("input the width: ")
h = input("input the height: ")
c = input("input the cost: ")

print calCost(w, h, c)
