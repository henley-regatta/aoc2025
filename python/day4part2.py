#!/usr/bin/env python3
# Day 4 Part 2
# Printing Department Forklift Fun
# ---------------------------------------
# Rolls of paper (@) can be accessed by a
# forklift if there are <4 rolls of paper
# adjacent.
#
# Play an iterative game whereby we remove
# the accessible rolls until we can do it
# no more.

import copy

datafile="data/day4.txt"

#########################################################
# visualisation
def dumpMap(papermap) :
    for row in papermap :
        r1=''.join(list(map(str,row)))
        print(r1.replace('2','x').replace('1','@').replace('0','.'))
        
#########################################################
# Update the map for next run
def updateMap(orgmap,accessList) :
    newMap=copy.copy(orgmap)
    for elem in accessList :
        newMap[elem[1]][elem[0]] = 0
    return newMap

#########################################################
# guts of it - work out neighbours
def getNeighbourCount(x,y,pmap) :
    sumNeighbour=0
    for cy in range(y-1,y+2) :
        for cx in range(x-1,x+2) :
            sumNeighbour += pmap[cy][cx]
    return sumNeighbour-1 # exclude "ourselves" in the middle

#########################################################
# Map Iterator
def iterateOverMap(pmap) :
    accessible=[]
    for y in range(1,len(pmap)-1) :
        for x in range(1,len(pmap[0])-1) :
            if pmap[y][x] == 1:
                neighbourCount = getNeighbourCount(x,y,pmap)
                if neighbourCount < 4:
                    accessible.append([x,y])
    return accessible

#########################################################
#########################################################
#########################################################
if __name__ == "__main__" :
    #Input is a "map" of @ and . lines. We can turn it
    #into a simple list. Because we need to look at neighbours
    #we'll grow the borders at each edge
    rollmap=[]
    with open(datafile,'r') as df :
        for line in df :
            nstr = line.strip().replace('@','1').replace('.','0')
            #Grow the line with a border of empty space
            nstr = "0" + nstr + "0"
            rollmap.append(list(map(int,list(nstr))))
    #prepend and append a row of blanks
    blankline = [0] * len(rollmap[0])
    rollmap.insert(0, blankline)
    rollmap.append(blankline)
    
    removeCount=0
    iterCount=1
    RollAgain=True
    while RollAgain :
        reachableRolls = iterateOverMap(rollmap)
        rollmap = updateMap(rollmap,reachableRolls)
        if len(reachableRolls) > 0 :
            removeCount += len(reachableRolls)
        else : 
            RollAgain = False 
        print(f"{iterCount} - Removed {len(reachableRolls)}")
        iterCount+=1
    print(f"Day4Part2 Answer: {removeCount}")