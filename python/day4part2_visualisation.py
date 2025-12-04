#!/usr/bin/env python3
# Day 4 Part 2
# Printing Department Forklift Fun
# ---------------------------------------
# EXTRA CREDIT - Do a visualisation of the 
# results

# assemble into a slow movie using:
#    ffmpeg -framerate 4 -f image2 -i visualisation/day4part2_%d.png -c:v libvpx-vp9 -pix_fmt yuva420p visualisation/aoc2025_day4part2.webm

# Rolls of paper (@) can be accessed by a
# forklift if there are <4 rolls of paper
# adjacent.
#
# Play an iterative game whereby we remove
# the accessible rolls until we can do it
# no more.
from PIL import Image,ImageDraw
import os
import copy

datafile="data/day4.txt"

visPrefix="visualisation/day4part2_"

#########################################################
# visualisation
def dumpMap(papermap, pngfile) :
    oX = len(papermap[0])-2
    oY = len(papermap)-2
    #We PIL now fam...
    img = Image.new(mode="RGB", size=(oX,oY), color = (255,255,255))
    drw = ImageDraw.Draw(img,'RGB')
    for y in range(1,len(papermap)-1) : # skip the border rows
        for x in range(1,len(papermap[0])-1) : # and the border columns
            p = papermap[y][x]
            if p == 1 : #Remaining roll (black)
                drw.point((x-1,y-1),fill=(0,0,0))
            elif p == -1 : #Roll to be removed (red)
                drw.point((x-1,y-1),fill=(255,0,0))
    #Now re-size the final image
    nX = oX * 2
    nY = oY * 2
    scaledimg = img.resize((nX,nY))
    scaledimg.save(pngfile)

#########################################################
# pre-vis update for "to be removed"
def preVisUpdate(orgmap,accessList) :
    visMap=copy.copy(orgmap)
    for e in accessList :
        visMap[e[1]][e[0]] = -1 # code for "remove me"
    return visMap
        
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
    
    dumpMap(rollmap,visPrefix + "0.png")
    
    removeCount=0
    iterCount=1
    RollAgain=True
    while RollAgain :
        reachableRolls = iterateOverMap(rollmap)
        dumpMap(preVisUpdate(rollmap,reachableRolls),f"{visPrefix}{iterCount}.png")
        iterCount+=1
        rollmap = updateMap(rollmap,reachableRolls)
        if len(reachableRolls) > 0 :
            removeCount += len(reachableRolls)
        else : 
            RollAgain = False 
        print(f"{iterCount//2} - Removed {len(reachableRolls)}")
        dumpMap(rollmap,f"{visPrefix}{iterCount}.png")
        iterCount+=1
    print(f"Day4Part2 Answer: {removeCount}")