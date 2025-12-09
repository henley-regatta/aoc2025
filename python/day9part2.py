#!/usr/bin/env python3
# Day 9 part 2
# Movie Theater Floor Tiles
# ------------------------------
# Find the biggest rectangle made
# from red tile corners but totally
# containing green tiles
from PIL import Image, ImageDraw
import copy

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
def findBoundary(points) :
    #find boundary x/y
    minC=[999999999,99999999]
    maxC=[0,0]
    for p in points :
        if p[0]>maxC[0] :
            maxC[0] = p[0]
        if p[1]>maxC[1] :
            maxC[1] = p[1]
        if p[0] < minC[0] :
            minC[0]=p[0]
        if p[1] < minC[1] :
            minC[1] = p[1]
    return [minC,maxC]

###############################################
def rankPoints(points) :
    ranked = copy.deepcopy(points)
    #append tag giving original order
    for i in range(0,len(ranked)) :
        ranked[i].append(i)
    #sort by x coordinate
    ranked.sort(key=lambda x: x[0])
    i=-1
    pr=-1
    for p in ranked :
        if p[0]!=pr :
            i+=1
            pr=p[0]
            p[0]=i 
        else :
            p[0]=i 
    #sort by y coordinate
    ranked.sort(key=lambda x: x[1])
    i=-1
    pr=-1
    for p in ranked :
        if p[1]!=pr :
            i+=1
            pr=p[1]
            p[1]=i
        else :
            p[1]=i
    #Re-sort back into original index order
    ranked.sort(key=lambda x: x[2])
    #get rid of the index
    for i in range(0,len(ranked)) :
        del ranked[i][-1]
    return ranked

###############################################
def pointsToTuples(points,offX,offY) :
    tuples=[]
    for p in points :
        tuples.append((p[0]-offX,p[1]-offY))
    return tuples
    
###############################################
#Produce a polygon as image from a list of points
def plotPoly(points, filename) :
    bounds=findBoundary(points)
    #Simple offset of points by min values
    dimX = (bounds[1][0] - bounds[0][0])+1
    dimY = (bounds[1][1] - bounds[0][1])+1
    print(f"Producing Poly image in {filename} dimensions X={dimX} Y={dimY}")
    offX = bounds[0][0]
    offY = bounds[0][1]
    im = Image.new('RGB',(dimX,dimY),(0,0,0))
    d = ImageDraw.Draw(im)
    pTuples = pointsToTuples(points,offX,offY)
    #Make 2 passes over the points data, first we do the polygon:
    d.polygon(pTuples,fill=(0,255,0),outline=(0,255,0))
    #and now do the points
    d.point(pTuples,fill=(255,0,0))
    
    #Write the image out
    im.save(filename)
        
    #send the data back as a 2d list of rows collapsing all non-white to
    #black
    d.point(pTuples,fill=(0,255,0))
    pixels=list(im.getdata(1))
    w,h=im.size
    pixels = [pixels[i*w:(i+1) * w] for i in range(h)]
    return pixels

###############################################
#there are far better algos for this but man
#am I tired.
def stupidInsideOutside(poly,minX,minY,maxX,maxY) :
    #if all 4 lines are within the poly, it's a hit
    #PROTIP: check left/right verticals first
    for y in range(minY,maxY+1) :
        if poly[y][minX] != 255 or poly[y][maxX] != 255 :
            return False
    #now the horizontals
    for x in range(minX,maxX+1) :
        if poly[minY][x] != 255 or poly[maxY][x] != 255 :
            return False
    return True

###############################################
def sortMyRec(points,i1,i2) :
    x1=points[i1][0]
    x2=points[i2][0]
    y1=points[i1][1]
    y2=points[i2][1]
    if x1>x2 :
        minX=x2
        maxX=x1
    else :
        minX=x1
        maxX=x2
    if y1>y2 :
        minY=y2
        maxY=y1
    else :
        minY=y1
        maxY=y2
    return [minX,minY,maxX,maxY]

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

    #report
    print(f"Read in {len(redtiles)} redtiles")
    #rank by position
    rankedTiles=rankPoints(redtiles)
    #get the poly from this
    poly=plotPoly(rankedTiles,'visualisation/day9part2_poly.png')
    print(f"poly image is {len(poly[0])} by {len(poly)}")
    
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
    print(f"{len(aList)} Psuedo-areas found")
    for area in aList:
        #we just need pseudo-ranges here
        (minX,minY,maxX,maxY) = sortMyRec(rankedTiles,area[1],area[2])
        if stupidInsideOutside(poly,minX,minY,maxX,maxY) :
            print(f"WINNRAR! - Area {area[0]} between {redtiles[area[1]]} and {redtiles[area[2]]}")
            exit()
        else :
            print(f"DISCARD area {area[0]} between {redtiles[area[1]]} and {redtiles[area[2]]}")

    #Now we descend the list until we find one that's completely enclosed within the green area    

    print(f"Biggest area found: {aList[0][0]} between {redtiles[aList[0][1]]} and {redtiles[aList[0][2]]}")