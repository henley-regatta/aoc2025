#!/usr/bin/env python3
# Day 7 part 2
# Laboratories and Teleportation
# ------------------------------
# Fix the transporter by examining 
# the tachyon manifold. 
# 
# Part 2: work out how many paths
# the beam can take

datafile="data/day7.txt"


#First do Part 1 because we need to know where the paths are

###############################################
def dumpBmap(line,bmap) :
    sline = list(line)
    for i in range(0,len(sline)) :
        if bmap[i] == 1 :
            sline[i] = "|"
        elif bmap[i] == -1 :
            sline[i] = "+"
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
pmap = []
pmap.append(bmap)
#now iterate of the rest of the map
for l in tmap :
    #reset previous splitter recording
    bmap = list(map(lambda x: 0 if x==-1 else x, bmap))
    #Find any splitters
    spos = [pos for pos, char in enumerate(l) if char == "^"]
    #update beam positions IF the beam impacts a splitter
    for sp in spos :
        if bmap[sp] == 1 :
            #Update position
            bmap[sp] = -1
            bmap[sp-1] = 1
            bmap[sp+1] = 1
    pmap.append(bmap)
    #print(dumpBmap(l,bmap))
    
#OK to calculate the paths we have to backtrack from the bottom
pmap.reverse()
for y in range(0,len(pmap)) :
    row = pmap[y]
    #first update the row from previous
    for x in range(0,len(row)) :
        if y>0 and row[x] != -1 :
            row[x] = pmap[y-1][x]
    #now combine if splitter
    for x in range(0,len(row)) :
        if row[x] == -1:  #it's a splitter, so it becomes the sum of the values left/right
            row[x] = row[x-1] + row[x+1]

#NOTE: This doesn't zero-out values as we progress back up the tree but this doesn't matter
#because they're "unreachable" later one. Our answer is the LARGEST number in the final line
    
print(f"Day 7 part 2 answer: {max(pmap[-1])}")