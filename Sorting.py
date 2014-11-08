###########################################
# Author: klion26
# Date: 2014/11/08
# Problem: Sorting
###########################################

# bubble sort
def bubbleSort(l):
    t = len(l)
    for i in xrange(t):
        j = t-1
        while j > i:
            if l[j]<l[j-1]:
                l[j],l[j-1] = l[j-1],l[j]
            j -= 1
    for i in l:
        print i,

# merge sort
def mergeSort(l):
    t = len(l)
    if t>1:
        # sort the left half
        a = l[0:t/2]
        print a
        a = mergeSort(a)
        # sort the right half
        b = l[t/2:]
        print b
        b = mergeSort(b)
        # merge left and right part
        i=0
        j=0
        l=[]
        while i<t/2 and j<t-t/2:
            if a[i]<b[j]:
                l.append(a[i])
                i += 1
            else:
                l.append(b[j])
                j += 1
        print l
        while i<t/2:
            l.append(a[i])
            i += 1
        print l
        while j<t-t/2:
            l.append(b[j])
            j += 1
        print l
        return l
    else:
        return l
if __name__ == "__main__":
    l = []
    n = input("Input the array numbers: ")
    while n:
        t = input()
        n -= 1
        l.append(t)
    print "while over"
    #bubbleSort(l)
    l = mergeSort(l)
    for i in l:
        print i,
