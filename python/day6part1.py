#!/usr/bin/env python3
# Day 6 part 1
# Trash Compactor Maths Tests
# ------------------------------
# Help the youngest cephalopod with her 
# maths homework. Simple addition & multiplication
# only the data is columnular.
#
# This is basically a parsing problem, right?

datafile="data/day6.txt"


###############################################
###############################################
###############################################
if __name__ == "__main__" :
    problems=[]
    operands=[]
    pcount=-1
    with open(datafile,'r') as df:
        for line in df:
            columns = line.strip().split()
            if pcount==-1 :
                pcount=len(columns)
                for x in range(0,pcount) :
                    problems.append([])
            for i in range(0,len(columns)) :
                if columns[i] in '*+' :
                    operands.append(columns[i].strip())
                else :
                    problems[i].append(int(columns[i].strip()))
    bigSum = 0
    for i in range(0,len(problems)) :
        pTot=problems[i][0]
        for j in range(1,len(problems[i])) :
            if operands[i] == '*' :
                pTot = pTot * problems[i][j]
            else :
                pTot = pTot + problems[i][j]
        print(f"Problem {i} with operand={operands[i]} and data {problems[i]} has result {pTot}")
        bigSum += pTot
    print(f"Day 6 Part 1 answer =  {bigSum}")
        
                    