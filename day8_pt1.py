f = open("data.txt", "r")

line = f.readline()

dat = []

res0 = []
res1 = []
res2 = []
res3 = []


visCount = 0

while line:
    dat.append([])
    for i in line[:-1]:
        dat[-1].append(int(i))
    res0.append([-1] * len(line[:-1]))
    res1.append([-1] * len(line[:-1]))
    res2.append([-1] * len(line[:-1]))
    res3.append([-1] * len(line[:-1]))
    line = f.readline()



def scanLeft(r, c):
    global res0
    global dat
    if(res0[r][c] != -1):
        return res0[r][c]
    if(r == 0 or c == 0 or r == len(dat)-1 or c == len(dat[0])):
        res0[r][c] = dat[r][c]
        return dat[r][c]
  
    res0[r][c] = max(dat[r][c], scanLeft(r,c-1))
    return res0[r][c]



def scanUp(r, c):
    global res1
    global dat
    if(res1[r][c] != -1):
        return res1[r][c]
    if(r == 0 or c == 0 or r == len(dat)-1 or c == len(dat[0])):
        res1[r][c] = dat[r][c]
        return dat[r][c]

    res1[r][c] = max(dat[r][c], scanUp(r+1,c))
    return res1[r][c]




def scanRight(r, c):
    # print(f"coor: {r}, {c}, for len={len(dat[0])}")
    global res2
    global dat
    if(res2[r][c] != -1):
        return res2[r][c]
    if(r == 0 or c == 0 or r == len(dat)-1 or c == len(dat[0])-1):
        res2[r][c] = dat[r][c]
        return dat[r][c]

    res2[r][c] = max(dat[r][c], scanRight(r,c+1))
    return res2[r][c]


def scanDown(r, c):
    global res3
    global dat
    if(res3[r][c] != -1):
        return res3[r][c]
    if(r == 0 or c == 0 or r == len(dat)-1 or c == len(dat[0])):
        res3[r][c] = dat[r][c]
        return dat[r][c]

    res3[r][c] = max(dat[r][c], scanDown(r-1,c))
    return res3[r][c]



for row in range(0,len(dat)):
    for col in range(0, len(dat[0])):
        if(row == 0 or col == 0 or row == len(dat)-1 or col == len(dat[0])-1):
            visCount += 1
        else:
            x = min(scanLeft(row, col-1), 
                    scanUp(row+1, col), 
                    scanRight(row, col+1),
                    scanDown(row-1, col))
            if(dat[row][col] > x):
                visCount += 1

print(visCount)


f.close()


