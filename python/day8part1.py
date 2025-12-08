#!/usr/bin/env python3
# Day 8 part 1
# Playground Junction Boxes
# ------------------------------
# Travelling Salesman Lite.
# Calculate the product of the 3 largest
# circuit sizes for <1000 connections.
# noting that we can "merge" connection 
# strings (oy vey)

datafile="data/day8.txt"
#need this many distinct connections
cMax = 1000

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
    print(f"{len(dList)} found and sorted")

    #And we'll now want to merge the N shortest pairs:
    mergeList = dList[0:cMax]
        
    #And now we need to make "strings" of connection pairs
    #(actually these are sets)
    circuits=[]
    for i in range(0,len(mergeList)) :
        f = mergeList[i][1]
        t = mergeList[i][2]
        print(f"{i} [{f},{t}]",end="...")
        pF = indexOfCircuit(circuits,f)
        pT = indexOfCircuit(circuits,t)
        if pF==-1 and pT==-1 :
            #Simples. New circuit
            circuits.append({f,t})
            print("new circuit")
        elif pF==-1 :
            circuits[pT].add(f)
            print(f"appending {f} to make {circuits[pT]}")
        elif pT==-1 :
            circuits[pF].add(t)
            print(f"appending {t} to make {circuits[pF]}")
        elif pF == pT :
            print(f"no need to do anything, contained in {circuits[pF]}")
        else :
            print(f"merged {circuits[pF]} and {circuits[pT]}",end=" ")
            circuits[pF].update(circuits[pT])
            del circuits[pT]
            print(f"making {circuits[pF]}")


    #From this list find the 3 biggest circuits
    cLength=[]
    for c in circuits :
        cLength.append(len(c))
    #Sort it
    cLength.sort(reverse=True)
    #3 biggest is then
    biggestCircuits = cLength[0:3]
    print(biggestCircuits)
    print(f"Day 8 Part 1 Answer :    {biggestCircuits[0]*biggestCircuits[1]*biggestCircuits[2]}")
            