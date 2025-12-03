#!/usr/bin/env python3
# Escalator Battery Power Restoration Fun
# ---------------------------------------
# Batteries are arranged into banks (lines of text)
# numbered 1-9 to indicate power level.
# 12 cells must be turned on from each bank. The power
# level is the concatanation of the power of each cell.
# (read from left-right with no swapsies)
# GOAL : Maximise the power level of each bank
# Return the sum of these power levels across each bank.

datafile="data/day3.txt"

#########################################################
def maxValInSubset(bank,start,maxIndex) :
    mVi=-1
    subset = bank[start:len(bank)-(maxIndex-1)]
    for t in [9,8,7,6,5,4,3,2,1] :
        for i in range(0,len(subset)) : 
            if subset[i] == t :
                mVi=i
                break
        if mVi != -1 :
            break
    if mVi == -1:
        print(f"error: scanned {subset} didn't find a biggest number")
        exit()
    #print(f"{subset} -> {subset[mVi]},({mVi})")
    return [subset[mVi],mVi]

#########################################################
def maxJoltage(bank) :
    #Now we have to do this for 12 biggest numbers
    maxVals=[]
    lastI=0
    for i in range(12,0,-1) :
        v = maxValInSubset(bank,lastI,i)
        lastI += v[1]+1
        maxVals.append(v[0])
    #I know this is a number but dear god it's easier to do this:
    mvstrs=map(str,maxVals)
    mvstr = ''.join(mvstrs)
    return int(mvstr)


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
        print(f"{foundMax}    {''.join(map(str,bank))}")
        
    print(f"part2 answer:  {sumMax}")