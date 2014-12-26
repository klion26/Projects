#count the Fibonacci Sequence
def Fibonacci(vec, n):
    #get the length of vec(the Fibonacci Sequence)
    l = len(vec)
    #generate the new sequence
    if  l<n:
        i = l
        while i < n:
            # the first and the second number
            if i==0 or i==1:
                vec.append(1)
            else:
                # other Fibonacci numbers
                vec.append(vec[i-1]+vec[i-2])
            # update i, be careful!!!{++i is wrong}!!!
            i += 1

# init a empty list            
vec = []
# calculate the Fibonacci Sequence
Fibonacci(vec, 10)
# print the Fibonacci Sequence
for i in vec:
    print i
