# Unable to solve :(
f = open("data.txt", "r")

line = f.readline()

# rope = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
rope = [[15,11], [15,11], [15,11], [15,11], [15,11], [15,11], [15,11], [15,11], [15,11], [15,11]]


visted = set()

visted.add((15,11))

count = 0

while line:
    times = int(line[2:])
    count += 1
    if(line[0] == 'R'):
        for j in range(times):
            rope[0][1] = rope[0][1] + 1
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
                
               
            visted.add(tuple(rope[9]))



        
    elif(line[0] == 'U'):
        for j in range(times):
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

            visted.add(tuple(rope[9]))
        
    elif(line[0] == 'L'):
        for j in range(times):
            rope[0][1] -= 1
            for i in range(1,10):
                rad = (rope[i-1][0] - rope[i][0]) * (rope[i-1][0] - rope[i][0]) + (rope[i-1][1] - rope[i][1]) * (rope[i-1][1] - rope[i][1])
                # Case 1:
                if(rope[i-1][0] == rope[i][0] and rope[i][1] > rope[i-1][1]+1):
                    rope[i][1] -= 1
                    if(count == 3):
                        print(f"{i} moved straight left")
                # Case 2:
                elif(rad >= 4):
                    if(rope[i][0] < rope[i-1][0]):
                        rope[i][0] += 1
                        rope[i][1] -= 1
                        print(f"{i} moved diagonal DL")
                    else:
                        rope[i][0] -= 1
                        rope[i][1] -= 1
                        print(f"{i} moved diagonal UL")

            visted.add(tuple(rope[9]))
            if(count == 3):
                for row in range(0, 21):
                    for col in range(0, 26):  
                        if(row == rope[0][0] and col == rope[0][1]):
                            print("H",end="")
                        elif(row == rope[1][0] and col == rope[1][1]):
                            print("1",end="")
                        elif(row == rope[2][0] and col == rope[2][1]):
                            print("2",end="")
                        elif(row == rope[3][0] and col == rope[3][1]):
                            print("3",end="")
                        elif(row == rope[4][0] and col == rope[4][1]):
                            print("4",end="")
                        elif(row == rope[5][0] and col == rope[5][1]):
                            print("5",end="")
                        elif(row == rope[6][0] and col == rope[6][1]):
                            print("6",end="")
                        elif(row == rope[7][0] and col == rope[7][1]):
                            print("7",end="")
                        elif(row == rope[8][0] and col == rope[8][1]):
                            print("8",end="")
                        elif(row == rope[9][0] and col == rope[9][1]):
                            print("9",end="")
                        else:
                            print(".",end="")
                    print()
                print("---")                
                

        
    elif(line[0] == 'D'):
        for j in range(times):
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
            visted.add(tuple(rope[9]))
    

    line = f.readline()



# print(len(test))
# print(rope)

f.close()