
f = open("data.txt", "r")

line = f.readline()

dat = []


maxCount = 0

while line:
    dat.append([])
    for i in line[:-1]:
        dat[-1].append(int(i))

    line = f.readline()



def scanLeft(r, c, treeVal):
    global dat
    if(dat[r][c] >= treeVal):
        return 1
    if(c == 0):
        return 1
    return 1 + scanLeft(r, c-1, treeVal)


def scanRight(r, c, treeVal):
    global dat
    if(dat[r][c] >= treeVal):
        return 1 
    if(c == len(dat[0]) - 1):
        return 1
    return 1 + scanRight(r, c+1, treeVal)
    

def scanUp(r, c, treeVal):
    global dat
    if(dat[r][c] >= treeVal):
        return 1
    if(r == 0):
        return 1
    return 1 + scanUp(r-1, c, treeVal)
    

def scanDown(r, c, treeVal):
    global dat
    if(dat[r][c] >= treeVal):
        return 1 
    if(r == len(dat)-1):
        return 1
    return 1 + scanDown(r+1, c, treeVal)
    

    

for row in range(0,len(dat)):
    for col in range(0, len(dat[0])):
        if(row == 0 or col == 0 or row == len(dat)-1 or col == len(dat[0])-1):
            pass
        else:
            x = scanLeft(row, col-1, dat[row][col]) * scanRight(row, col+1, dat[row][col]) * scanUp(row-1, col, dat[row][col])  * scanDown(row+1, col, dat[row][col]) 
            maxCount = max(maxCount, x)

print(maxCount)


f.close()
