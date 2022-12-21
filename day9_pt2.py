f = open("data.txt", "r")

line = f.readline()

rope = [[0,0]] * 10


visted = set()

visted.add(tuple(rope[0]))


while line:
    times = int(line[2:])
    if(line[0] == 'R'):
        for i in range(times):
            rope[0][1] += 1
            for i in range(1, 10):
                rad = (rope[i-1][0] - rope[i][0]) * (rope[i-1][0] - rope[i][0]) + (rope[i-1][1] - rope[i][1]) * (rope[i-1][1] - rope[i][1])
                # Case 1:
                if(rope[i-1][0] == rope[i][0] and rope[i][1] < rope[i-1][1]-1):
                    rope[i][1] += 1
                # Case 2:
                elif(rad >= 4):
                    if(rope[i][0] < rope[i-1][0]):
                        rope[i][0] += 1
                        rope[i][1] += 1
                    else:
                        rope[i][0] -= 1
                        rope[i][1] += 1
                
                visted.add(tuple(rope[i]))



        
    elif(line[0] == 'U'):
        for i in range(times):
            rope[0][0] -= 1
            for i in range(1,10):
                rad = (rope[i-1][0] - rope[i][0]) * (rope[i-1][0] - rope[i][0]) + (rope[i-1][1] - rope[i][1]) * (rope[i-1][1] - rope[i][1])
                # Case 1:
                if(rope[i-1][1] == rope[i][1] and rope[i][0] > rope[i-1][0]+1):
                    rope[i][0] -= 1
                # Case 2:
                elif(rad >= 4):
                    if(rope[i][1] < rope[i-1][1]):
                        rope[i][0] -= 1
                        rope[i][1] += 1
                    else:
                        rope[i][0] -= 1
                        rope[i][1] -= 1

                visted.add(tuple(rope[i]))
        
    elif(line[0] == 'L'):
        for i in range(times):
            rope[0][1] -= 1
            for i in range(1,10):
                rad = (rope[i-1][0] - rope[i][0]) * (rope[i-1][0] - rope[i][0]) + (rope[i-1][1] - rope[i][1]) * (rope[i-1][1] - rope[i][1])
                # Case 1:
                if(rope[i-1][0] == rope[i][0] and rope[i][1] > rope[i-1][1]+1):
                    rope[i][1] -= 1
                # Case 2:
                elif(rad >= 4):
                    if(rope[i][0] < rope[i-1][0]):
                        rope[i][0] += 1
                        rope[i][1] -= 1
                    else:
                        rope[i][0] -= 1
                        rope[i][1] -= 1

                visted.add(tuple(rope[i]))
                
                

        
    elif(line[0] == 'D'):
        for i in range(times):
            rope[0][0] += 1
            for i in range(1, 10):
                rad = (rope[i-1][0] - rope[i][0]) * (rope[i-1][0] - rope[i][0]) + (rope[i-1][1] - rope[i][1]) * (rope[i-1][1] - rope[i][1])
                # Case 1:
                if(rope[i-1][1] == rope[i][1] and rope[i][0] < rope[i-1][0]-1):
                    rope[i][0] += 1
                # Case 2:
                elif(rad >= 4):
                    if(rope[i][1] < rope[i-1][1]):
                        rope[i][0] += 1
                        rope[i][1] += 1
                    else:
                        rope[i][0] += 1
                        rope[i][1] -= 1
            visted.add(tuple(rope[i]))
        
                
    line = f.readline()



print(rope)
print(len(visted))

f.close()