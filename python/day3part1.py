#!/usr/bin/env python3
# Escalator Battery Power Restoration Fun
# ---------------------------------------
# Batteries are arranged into banks (lines of text)
# numbered 1-9 to indicate power level.
# 2 cells must be turned on from each bank. The power
# level is the concatanation of the power of each cell.
# (read from left-right with no swapsies)
# GOAL : Maximise the power level of each bank
# Return the sum of these power levels across each bank.

datafile="data/day3.txt"

#########################################################
def maxJoltage(bank) :
    #find the furthest-left largest number
    m1i=-1
    for t in [9,8,7,6,5,4,3,2,1] :
        for i in range(0,len(bank)-1) : #can't get the last number, need 2 in output
            if bank[i] == t :
                m1i=i
                break
        if m1i != -1 :
            break 
    #Find the largest number to the right of this position
    m2i=-1
    for t in [9,8,7,6,5,4,3,2,1] :
        for i in range(m1i+1,len(bank)) :
            if bank[i] == t :
                m2i=i
                break
        if m2i != -1 :
            break
    
    return bank[m1i]*10 + bank[m2i]


#########################################################
#########################################################
#########################################################
if __name__ == "__main__" :
    #parse the input into a list of nums
    powerwall=[]
    with open(datafile,'r') as df:
        for line in df:
            bank = list(map(int,list(line.strip())))
            powerwall.append(bank)
    sumMax=0
    for bank in powerwall :
        foundMax = maxJoltage(bank) 
        sumMax+=foundMax
        print(f"{foundMax}    {bank}")
        
    print(f"part1 answer:  {sumMax}")