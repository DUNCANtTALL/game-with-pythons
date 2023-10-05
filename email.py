import random
import math

list = ["2"," 3", "5", "7", "11", "13", "17", "19", "23", "29", "31", "37", "41", "43", "47", "53", "59", "61", "67", "71", "73", "79", "83", "89", "97"]

def search(val):
    for i in list:
        if i == str(val):
            return True
    return False

print(search(5))  # Output: True

high=list[0]
low=list[-1]
n=(int)(2*int(high)+int(low))//2
print(n)
def binary_search(val=53):
    while high>low :
        n = (int)(2 * int(high) + int(low)) // 2
        if n==val :
            return True
            return n
        elif val>n :
            low=n+1
        elif val<n :
            high = n -1
    return False







