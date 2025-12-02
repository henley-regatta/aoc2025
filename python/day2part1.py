#!/usr/bin/env python3
# Invalid IDs in the North Pole Gift Shop database
# ------------------------------------------------
# Invalid IDs have a repeating sequence of numbers
# OR start with a 0. 
# Ids are provided as a range X-Y where every number
# within that range is a candidate to check.
#  * In the range 11-22, both 11 and 22 are invalid but 
#    all other values (12,13...20,21) are valid
#  * In the range 1188511880-1188511890, the only invalid number 
#    is 1188511885
# The answer is the sum of invalid numbers
# Input is a comma-separated list of ID ranges

datafile="data/day2.txt"

############################################################
# This is the simplest but stupidest way I can think of doing
# this....
def strCompNum(number) :
    numStr = str(number)
    l = len(numStr)
    if l%2 != 0 :
        return False
    p1=numStr[0:l//2]
    p2=numStr[l//2:]
    return p1==p2

#Step one is to read the data and split into ranges. We can
#evaluate each range separately
with open(datafile,'r') as df :
    ranges = df.read().strip().split(',')
print(f"Found {len(ranges)} ranges to check")

sumInvalid=0
for r in ranges :
    (min,max) = r.split('-',2)
    print(f"checking range {min} - {max}")
    for x in range(int(min),int(max)+1) :
        if strCompNum(x) :
            print(f"{x} invalid")
            sumInvalid+=x 

print(f"Your answer is: {sumInvalid}")