#!/usr/bin/env python3
# Day 6 part 2
# Trash Compactor Maths Tests
# ------------------------------
# Help the youngest cephalopod with her 
# maths homework. Simple addition & multiplication
# only the data is columnular. Like, really columnular.
#
# This is an ugly parsing problem because a) column position
# is important within a problem b) columns aren't fixed width
#
# Luckily, the position of the operand in the final line provides
# a positional marker for the data boundary. Have to reach that first

datafile="data/day6.txt"

###############################################
###############################################
###############################################
if __name__ == "__main__" :
    lines=[]
    opos=[]
    operands=[]
    #multiple passes required over the data. First, read it:
    with open(datafile,'r') as df:
        for line in df:
            lines.append(line)
    #Now iterate over the last line getting the POSITIONS of the
    #operands
    for i in range(0,len(lines[-1])) :
        if lines[-1][i]!=" " :
            opos.append(i)
            operands.append(lines[-1][i])
    #And then pass over the other lines extracting strings at positions
    nStrs=[]
    for i in range(0,len(opos)) :
        nStrs.append([])
    for l in range(0,len(lines)-1) :
        p=0
        line=lines[l]
        for i in range(1,len(opos)+1) :
            if i >= len(opos) :
                c = len(line)
            else :
                c =opos[i]
            number = line[p:c-1]
            nStrs[i-1].append(number)
            p=c 

    #And finally, build the actual numbers. msig is top, lsig at the bottom
    numbers=[]
    for x in nStrs :
        numbers.append([])
    for i in range(len(nStrs)-1,-1,-1) :
        nSet = nStrs[i]
        for x in range(len(nSet[0])-1,-1,-1) :
            number=''
            for j in range(0,len(nSet)) :    
                nStr = nSet[j]
                number += nStr[x]
            numbers[i].append(int(number))

    #This bit is the same for part 2, provided we've marshalled the
    #columns correctly....
    bigSum = 0
    for i in range(0,len(numbers)) :
        pTot=numbers[i][0]
        for j in range(1,len(numbers[i])) :
            if operands[i] == '*' :
                pTot = pTot * numbers[i][j]
            else :
                pTot = pTot + numbers[i][j]
        print(f"Problem {i} with operand={operands[i]} and data {numbers[i]} has result {pTot}")
        bigSum += pTot
    print(f"Day 6 Part 2 answer =  {bigSum}")
        
                    