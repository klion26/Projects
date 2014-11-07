###########################################
# Author: klion26
# Date: 2014/11/05
# Problem: Calculator
###########################################

# basic calculator(+, -, *, /)
def basicCal():
    num1 = input("Enter a number: ")
    num2 = input("Enter the second number: ")
    op = raw_input("Enter Operator (+, -, *, /): ")
    equation = "%d %s %d" % (num1, op, num2)
    # if the operator is invalid
    if op not in "+-*/":
        print "'" + op + "' is an invalid operator"
        basicCal()
    else:
        if op == "+":
            result =  num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        else:
            result = num1 / num2
        print "The result of your equation '%s' is: %d" % (equation, result)


if __name__ == "__main__":
    basicCal()
