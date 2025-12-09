#!/usr/bin/env python3
# Day 9 part 1
# Movie Theater Floor Tiles
# ------------------------------
# Find the biggest rectangle made
# from red tiles

datafile="data/day9.txt"


###############################################
def calcArea(p1,p2) :
    scalars=[]
    for i in [0,1] :
        if p1[i]>p2[i] :
            scalars.append(p1[i]-p2[i])
        else :
            scalars.append(p2[i]-p1[i])
    return (scalars[0]+1)*(scalars[1]+1)

###############################################
###############################################
###############################################
if __name__ == "__main__" :
    redtiles=[]
    #first load/parse our list of red tiles
    with open(datafile,'r') as df :
        for line in df:
            pStr = line.strip().split(',',2)
            redtiles.append(list(map(int,pStr)))
    #find boundary x/y
    minC=[999999999,99999999]
    maxC=[0,0]
    for p in redtiles :
        if p[0]>maxC[0] :
            maxC[0] = p[0]
        if p[1]>maxC[1] :
            maxC[1] = p[1]
        if p[0] < minC[0] :
            minC[0]=p[0]
        if p[1] < minC[1] :
            minC[1] = p[1]
    #report
    print(f"Read in {len(redtiles)} redtiles bounded at ({minC},{maxC})")
    
    print("Finding Areas",end="...")
    aList=[]
    for i in range(0,len(redtiles)) :
        for j in range(i,len(redtiles)) :
            if i == j : 
                continue
            a = calcArea(redtiles[i],redtiles[j])
            aList.append([a,i,j])

    #And so now we need the distances sorted
    aList.sort(key=lambda x: x[0], reverse=True)
    print(f"{len(aList)} areas found")
    
    #Biggest area is just the first off this list
    print(f"Biggest area found: {aList[0][0]} between {redtiles[aList[0][1]]} and {redtiles[aList[0][2]]}")