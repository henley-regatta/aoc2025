#!/usr/bin/env python3
# Day 7 part 1
# Laboratories and Teleportation
# ------------------------------
# Fix the transporter by examining 
# the tachyon manifold. 
# 
# Part 1: work out how many times 
# the beam will be split.

datafile="data/day7.txt"


###############################################
def dumpBmap(line,bmap) :
    sline = list(line)
    for i in range(0,len(sline)) :
        if bmap[i] == 1 :
            sline[i] = "|"
    return ''.join(sline)

###############################################
###############################################
###############################################
if __name__ == "__main__" :
    with open(datafile,'r') as df:
        tmap = df.readlines()

#NOTE: Data is kind. We know first/last columns are blank
#therefore we don't have to "grow" the borders this time

#find the start pos
spos = tmap[0].find('S')

#create a 1-line map of where the beams are
bmap = [0] * len(tmap[0])
bmap[spos] = 1

#now iterate of the rest of the map
foundSplitters=0
for l in tmap :
    #Find any splitters
    spos = [pos for pos, char in enumerate(l) if char == "^"]
    #update beam positions IF the beam impacts a splitter
    for sp in spos :
        if bmap[sp] == 1 :
            #Update position
            foundSplitters+=1
            bmap[sp] = 0
            bmap[sp-1] = 1
            bmap[sp+1] = 1
    print(dumpBmap(l,bmap))

print(f"Day 7 part 1 answer:    {foundSplitters}")
        

