#!/usr/bin/env python3
# Day 10 part 1
# Factory Machine Initialisation
# ------------------------------
# Given a set of desired output indicator lights,
# work out the lowest number of button pushes to 
# achieve the desired end state starting from all-off
import itertools
import math

datafile="data/day10.txt"


#######################################################
def parseFile(f) :
    lights=[]
    buttons=[]
    joltage=[]
    with open(f,'r') as inF:
        for line in inF:
            p1=line.strip().split()
            blist=[]
            for p in p1 :
                if '[' in p :
                    p = p.replace('[','').replace(']','').replace('.','0').replace('#','1')
                    oL=list(map(int,list(p)))
                    lights.append(oL)
                elif '(' in p:
                    p = p.replace('(','').replace(')','')
                    bL=p.split(',')
                    blist.append(list(map(int,bL)))
                elif '{' in p:
                    p = p.replace('{','').replace('}','')
                    jL=p.split(',')
                    joltage.append(list(map(int,jL)))
            buttons.append(blist)
    return lights,buttons,joltage

#######################################################
def runPermutation(tgt,buttons,sequence, limit) :
    state=[0]*len(tgt)
    ctr=0
    for s in sequence :
        ctr+=1
        if ctr == limit :
            return -1 #don't care about solution, it's over limit
        b = buttons[s]
        for i in b :
            state[i] = 1 - state[i]
        if state == tgt :
            return ctr
    return -1 # no solution found


#######################################################
# Solve for a particular machine
def findMinPushes(lights,buttons) :
    #generate permutations
    p0=[]
    for i in range(0,len(buttons)) :
        p0.append(i)
    maxPress = len(p0)
    foundMin = False
    tgtPress = 1
    print(f"Testing single-push iterations of length =",end=" ")
    while tgtPress <= len(p0) :
        print(tgtPress,end=" ")
        for perm in itertools.permutations(p0,tgtPress) :
            res = runPermutation(lights,buttons,perm,tgtPress)
            if res>0 :
                return res
        tgtPress+=1
            
    
    print(f"Probable Error - no solution found")
    exit()
    

#######################################################
#######################################################
#######################################################
if __name__ == "__main__" :
    (lights,buttons,joltage) = parseFile(datafile)
    #Part 1 is an iterative game over each "machine" so...
    sumSolutions=0
    print(f"Finding button presses for {len(lights)} Machines....")
    for i in range(0,len(lights)) :
        print(f"solving for machine {i}: lights = {lights[i]} buttons = {len(buttons[i])}")
        press = findMinPushes(lights[i],buttons[i])
        print(f"machine {i} solvable in {press} buttons")
        sumSolutions += press
    print(f"Day 10 Part 1 Answer: {sumSolutions}")
