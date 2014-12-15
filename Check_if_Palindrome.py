###########################################
# Author: klion26
# Date: 2014/11/16
# Problem: Check_if_Palindrome
###########################################

def palin(s):
    return s[::-1] == s

if __name__ == "__main__":
    s = raw_input("input a string  ")
    print palin(s)
