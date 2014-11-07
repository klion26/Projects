###########################################
# Author: klion26
# Date: 2014/11/07
# Problem: Credit_Card_Validator
###########################################

###########################################
# Algorithm: Luhn algorithm
# Step 1: Double the value of alternate digits of the primary account number beginning with the second digit from the right (the first right--hand digit is the check digit.)
# Step 2: Add the individual digits comprising the products obtained in Step 1 to each of the unaffected digits in the original number.
# Step 3: The total obtained in Step 2 must be a number ending in zero (30, 40, 50, etc.) for the account number to be validated.
###########################################

# test the card num is a valid or not
# !!!!we should add some other restrains such as prefix and length of card num!!!
def validCard(num):
    sum = 0
    # double every other number from the 2nd right most
    # and add it to the sum
    for i in num[-2::-2]:
        # double the digit
        # ord(i) --> get the ascii value of i
        # chr(i) --> get the character of value i
        t = 2*(ord(i) - ord('0'))
        if t > 9: # if t is bigger than 9, the add two digits of the number to sum
            t = t/10 + t%10
        sum += t
    # add every other number from the right most digit
    for i in num[-1::-2]:
        sum += ord(i) - ord('0')
    # if sum is zero-ending number
    if sum%10 == 0:
        print "A valid card number"
    else:
        print "Isnot a valid card number"

def validCard2(num):
    # reverse card number
    ss = num[::-1]
    # get a list contains the digits we doubled
    a = [int(ss[i])*2 for i in range(1, len(ss), 2)]
    # get a list contains the digits from ss
    b = [int(ss[i]) for i in range(0, len(ss), 2)]
    # process list a if needed(we need each digit, not the value),
    # change xy-->x+y
    c = [i/10+i%10 for i in a]
    # get the final sum
    e = sum(b)+sum(c)
    if e%10 == 0: # test the final sum
        print "A valid card"
    else:
        print "An invalid card"
    #print e

# same as validCard2
def validCard3(num):
    # change string to int list
    digits = [int(char) for char in num]
    # reverse
    digits = digits[-1::-1]

    # get the list of doubled
    doubled = [(digit*2) if ((i+1)%2 == 0) else digit\
               for (i, digit) in enumerate(digits)]
    # process each digit if needed
    summe = [num if num<10 else num-9 \
             for num in doubled]
    # test the sum
    if sum(summe)%10 ==0:
        print "A valid card"
    else:
        print "An invalid card"
if __name__ == "__main__":
    num = raw_input("Input the card number: ")
    validCard(num)
    validCard2(num)
    validCard3(num)
