#!/usr/bin/env python3
# We have a DIAL with numbers 0-99
# We have an INPUT which specifies a letter L/R for rotation
# and a number giving the number of steps to move
# We start from 50
#(this is just clock arithmetic, right?)

inputfile="data/day1.txt"

dialpos=50
dialmax=99
dialmin=0
range=(dialmax-dialmin)+1

with open(inputfile,'r') as fh:
    scount=0
    zerocount=0
    print(f"{scount:<6} Starting at {dialpos}")
    for move in fh:
        scount+=1
        dir=move[0]
        steps=int(move.strip()[1:])
        if steps > range : #sneaky wotsits always pull this trick
            print(f"SNEAKY reset {steps} to {steps%range}")
            steps = steps % range
        if dir == "L" :
            dialpos-=steps
            if dialpos<0 :
                dialpos = range+(dialpos)
        elif dir == "R" :
            dialpos+=steps
            if dialpos > dialmax :
                dialpos = dialpos % range
        if dialpos == 0 :
            zerocount+=1
        print(f"{scount:<6} {dir} {steps} to {dialpos}")
print(f"Password: {zerocount}")