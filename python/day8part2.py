#!/usr/bin/env python3
# Day 8 part 2
# Playground Junction Boxes
# ------------------------------
# Travelling Salesman Lite.
# Keep merging the sample set until you end up with
# all junction boxes in a single circuit.
# Report the product of the X coordinates of the 
# last 2 boxes merged to make this connection

datafile="data/day8.txt"

###############################################
def calcDistanceSquared(p1,p2) :
    dSquared=0
    for i in [0,1,2] :
        if p1[i]>p2[i] :
            dSquared += (p1[i]-p2[i]) ** 2
        else :
            dSquared += (p2[i]-p1[i]) ** 2
    return dSquared

###############################################
def indexOfCircuit(circuits,x) :
    for i in range(0,len(circuits)) :
        if x in circuits[i] :
            return i
    return -1

###############################################
###############################################
###############################################
if __name__ == "__main__" :
    points=[]
    with open(datafile,'r') as df :
        for line in df:
            p = line.strip().split(',')
            points.append(list(map(int,p)))
    #we want an inverse distance matrix - a set of 
    #distances with the 2 points they connect.
    print("Finding Distances",end="...")
    dList=[]
    for i in range(0,len(points)) :
        for j in range(i,len(points)) :
            if i == j : 
                continue
            d = calcDistanceSquared(points[i],points[j])
            dList.append([d,i,j])

    

    #And so now we need the distances sorted
    dList.sort(key=lambda x: x[0])
    numBPairs = len(dList)
    print(f"{numBPairs} found and sorted")
       
       
    numBoxes = len(points)
    
    #And now we need to make "strings" of connection pairs
    #(actually these are sets)
    circuits=[]
    usedAllIndicies=False
    usedIndicies=set()
    haveOneCircuit=False 
    lastBoxes=[-1,-1]
    i=0
    while i <= numBPairs :
        f = dList[i][1]
        t = dList[i][2]
        print(f"{i}/{numBPairs} [{f},{t}]",end="...")
        pF = indexOfCircuit(circuits,f)
        pT = indexOfCircuit(circuits,t)
        if pF==-1 and pT==-1 :
            #Simples. New circuit
            circuits.append({f,t})
            print("new circuit",end=" ")
        elif pF==-1 :
            circuits[pT].add(f)
            print(f"appending {f} to make {pT} len={len(circuits[pT])}",end="...")
        elif pT==-1 :
            circuits[pF].add(t)
            print(f"appending {t} to make {pF} len={len(circuits[pT])}",end="...")
        elif pF == pT :
            print(f"no need to do anything, contained in circuit {pF} of len={len(circuits[pF])}",end="...")
        else :
            print(f"merged circuits {pF} and {pT}",end=" ")
            circuits[pF].update(circuits[pT])
            print(f"making one of length {len(circuits[pF])}",end="...")
            del circuits[pT]
        if usedAllIndicies and len(circuits) == 1:
            haveOneCircuit = True 
            print("Merged all boxes into one circuit")
            lastBoxes = [f,t]
            break
        if not usedAllIndicies :
            usedIndicies.add(f)
            usedIndicies.add(t)
            if len(usedIndicies) == numBoxes :
                usedAllIndicies = True
                print(f"DEINHIBIT: all boxes now in play",end=" ")
            else:
                print(f"({len(usedIndicies)} / {numBoxes} used)",end=" ")

        print(f"circuits={len(circuits)}")
        i+=1
    
    if lastBoxes[0] == -1 :
        print(f"Failed to find a solution, circuits didn't merge still have {len(circuits)} remaining")
        exit()
        
    print(f"{lastBoxes} = {points[lastBoxes[0]]}, {points[lastBoxes[1]]}")
    #Get the X coordinates for these boxes
    X1 = points[lastBoxes[0]][0]
    X2 = points[lastBoxes[1]][0]
    #Answer we seek is the product of these
    print(f"Day 8 Part 2 Answer:     {X1*X2}")