###########################################
# Author: klion26
# Date: 2014/11/16
# Problem: Count_Vowels
###########################################

def vowels(s):
    v = [0]*5
    for i in s:
        if i=='a':
            v[0] = v[0]+1
        elif i=='e':
            v[1] = v[1]+1
        elif i=='i':
            v[2] = v[2]+1
        elif i=='o':
            v[3] = v[3]+1
        elif i=='u':
            v[4] = v[4]+1
        else:
            pass
    return v

if __name__ == "__main__":
    s = raw_input("input a string: ")
    print vowels(s)
