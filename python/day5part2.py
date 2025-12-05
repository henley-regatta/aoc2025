#!/usr/bin/env python3
# Day 5 Part s
# Cafeteria Inventory Management
# ------------------------------
# Given a list of fresh ingredient ranges,
# list the NUMBER of ingredients considered
# fresh
datafile="data/day5.txt"

###############################################
def parseInputFile(infile) :
    #two sets of data in one file, separated
    #by a blank line
    ranges=[]
    ingredients=[]
    with open(infile,'r') as df :
        for line in df :
            datum = line.strip()
            if '-' in datum :
                (rFrom,rTo) = datum.split('-',2)
                ranges.append([int(rFrom),int(rTo)])
            elif len(datum)>0 :
                ingredients.append(int(datum))
    return ranges,ingredients

###############################################
# I think this is needed for the big problem
# and it's a good idea anyway
def mergeRanges(ranges) :
    #first sort ranges by start point
    ranges.sort()
    #We start with the smollest
    res = []
    res.append(ranges[0])
    for i in range(1,len(ranges)) :
        last = res[-1]
        curr = ranges[i]
        #if current overlaps with last, merge
        if curr[0] <= last[1] :
            last[1] = max(last[1],curr[1])
        else :
            res.append(curr)
    return res
    
###############################################
###############################################
###############################################
if __name__ == "__main__" :
    (ranges,ingredients) = parseInputFile(datafile)
    print(f"Read {len(ranges)} ranges and {len(ingredients)} ingredients")
    fewestRanges=mergeRanges(ranges)
    print(f"collapsed to {len(fewestRanges)} non-overlapping ranges")
    sumFreshIDs=0
    for r in fewestRanges :
        sumFreshIDs += (r[1] - r[0])+1
    
    print(f"Day 5 Part 2 answer:   {sumFreshIDs}")