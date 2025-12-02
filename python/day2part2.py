#!/usr/bin/env python3
# Invalid IDs in the North Pole Gift Shop database
# ------------------------------------------------
# Invalid IDs have a repeating sequence of numbers
# OR start with a 0. 
# Sequences within the number must repeat AT LEAST twice
# Ids are provided as a range X-Y where every number
# within that range is a candidate to check.
#  * In the range 11-22, both 11 and 22 are invalid but 
#    all other values (12,13...20,21) are valid
#  * In the range 99-115, 99 and 111 are invalid
#  * In the range 1188511880-1188511890, the only invalid number 
#    is 1188511885
# The answer is the sum of invalid numbers
# Input is a comma-separated list of ID ranges

datafile="data/day2.txt"

############################################################
# This is still a stupid way of doing it....
def strCompNum(number) :
    numStr = str(number)
    
    for fLen in range(len(numStr)//2,0,-1) :
        #print(f"splitting {numStr} into fragments of length {fLen}")
        #Skip fragment if it doesn't go into the string length
        if len(numStr)%fLen != 0 :
            continue 
        p0=numStr[0:fLen]
        #print(f"p0 = {p0}")
        isPattern=True
        i0=fLen
        for i in range(fLen*2,len(numStr)+1,fLen) :
            pComp=numStr[i0:i]
            i0=i 
            #print(f"i = {i}, pComp = {pComp}")
            if pComp != p0 :
                isPattern=False
                break
        if isPattern :
            print(f"pattern: {pComp}")
            return True 
    
    return False

    

#Step one is to read the data and split into ranges. We can
#evaluate each range separately
with open(datafile,'r') as df :
    ranges = df.read().strip().split(',')
print(f"{len(ranges)} ranges to check")

sumInvalid=0
for r in ranges :
    (min,max) = r.split('-',2)
    print(f"checking range {min} - {max}")
    for x in range(int(min),int(max)+1) :
        if strCompNum(x) :
            print(f"\t{x} invalid")
            sumInvalid+=x 

print(f"Your answer is: {sumInvalid}")