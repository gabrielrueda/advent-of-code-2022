file = open("data.txt", "r")
line = file.readline()


cycleNum = 0
sumOfSignalStrengths = 0
x = 1

out = [""]

# visitCycles = {40, 80, 120, 160, 200, 240}

offset = 0

while(line):
    if(line[0] ==  "n"):
        if(x-1 <= cycleNum % 40 and x+1 >= cycleNum%40): 
            out.append("#")
        else:
            out.append(".")
        cycleNum += 1
        
    else:
        if(x-1 <= cycleNum%40 and x+1 >= cycleNum%40): 
            out.append("#")
        else:
            out.append(".")
        cycleNum += 1
        if(x-1 <= cycleNum%40 and x+1 >= cycleNum%40): 
            out.append("#")
        else:
            out.append(".")
        cycleNum += 1
        x += int(line[5:])
        

    line = file.readline()

file.close()

print(cycleNum)
print(len(out))

for i in range(0,240):
    print(out[i], end="") 
    if(i % 40 == 0): print()

