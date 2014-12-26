###########################################
# Author: klion26
# Date: 2014/11/07
# Problem: Alarm_Clock
###########################################
# import time library
import time
# define the alarm function
def alarm(n):
    # sleep n second(s)
    time.sleep(n)
    # print a message, wo could play a song
    print "Alarm Clock"


if __name__ == "__main__":
    # input the second(s) we want to sleep
    n = input("Input the second(s) you want to sleep: ")
    # call alarm(n)
    alarm(n)
