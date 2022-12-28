file = open("data.txt", "r")
line = file.readline()


cycleNum = 1
sumOfSignalStrengths = 0
x = 1

visitCycles = {20, 60, 100, 140, 180, 220}

while(line):
    if(line[0] ==  "n"):
        cycleNum += 1
        if(cycleNum in visitCycles): 
            sumOfSignalStrengths += (x * cycleNum)
    else:
        cycleNum += 1
        if(cycleNum in visitCycles): 
            sumOfSignalStrengths += (x * cycleNum)
        cycleNum += 1
        x += int(line[5:])
        if(cycleNum in visitCycles): 
            sumOfSignalStrengths += (x * cycleNum)

    line = file.readline()

file.close()

print(sumOfSignalStrengths)
