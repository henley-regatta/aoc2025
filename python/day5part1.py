#!/usr/bin/env python3
# Day 5 Part 1
# Cafeteria Inventory Management
# ------------------------------
# Given a list of fresh ingredient ranges,
# and a list of available ingredient IDs, 
# determine the number of fresh ingredients 
# in stock.
# NOTE: fresh range can overlap.
# This has the smell of needing to collapse 
# ranges before comparison.

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
# guts of the issue...
def isFresh(ingredient,ranges) :
    #SPECIAL CASES:
    if ingredient < ranges[0][0] :
        return False
    if ingredient > ranges[-1][1] :
        return False 
    #Find the range into which the ingredient *may* fit:
    for i in range(0,len(ranges)) :
        #iterate up until we find our range
        if ingredient > ranges[i][1] :
            continue # it's bigger than this range
        if ingredient >= ranges[i][0] :
            return True
        else :
            return False
    #we should never get here
    print(f"{ingredient} slipped through the cracks")
    exit()
    
###############################################
###############################################
###############################################
if __name__ == "__main__" :
    (ranges,ingredients) = parseInputFile(datafile)
    print(f"Read {len(ranges)} ranges and {len(ingredients)} ingredients")
    fewestRanges=mergeRanges(ranges)
    print(f"collapsed to {len(fewestRanges)} distinct ranges")
    freshIngredients=0
    for ingredient in ingredients :
        if isFresh(ingredient,fewestRanges) :
            freshIngredients += 1
    print(f"Day 5 Part 1 Answer: {freshIngredients}")