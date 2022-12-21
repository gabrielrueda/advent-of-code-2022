

f = open("data.txt", "r")

line = f.readline()

tail = [0,0]
head = [0,0]

visted = set()

visted.add(tuple(tail))


while line:
    times = int(line[2:])
    if(line[0] == 'R'):
        for i in range(times):
            head[1] += 1
            rad = (head[0] - tail[0]) * (head[0] - tail[0]) + (head[1] - tail[1]) * (head[1] - tail[1])
            # Case 1:
            if(head[0] == tail[0] and tail[1] < head[1]-1):
                tail[1] += 1
            # Case 2:
            elif(rad >= 4):
                if(tail[0] < head[0]):
                    tail[0] += 1
                    tail[1] += 1
                else:
                    tail[0] -= 1
                    tail[1] += 1
            
            visted.add(tuple(tail))



        
    elif(line[0] == 'U'):
        for i in range(times):
            head[0] -= 1
            rad = (head[0] - tail[0]) * (head[0] - tail[0]) + (head[1] - tail[1]) * (head[1] - tail[1])
            # Case 1:
            if(head[1] == tail[1] and tail[0] > head[0]+1):
                tail[0] -= 1
            # Case 2:
            elif(rad >= 4):
                if(tail[1] < head[1]):
                    tail[0] -= 1
                    tail[1] += 1
                else:
                    tail[0] -= 1
                    tail[1] -= 1

            visted.add(tuple(tail))
        
    elif(line[0] == 'L'):
        for i in range(times):
            head[1] -= 1
            rad = (head[0] - tail[0]) * (head[0] - tail[0]) + (head[1] - tail[1]) * (head[1] - tail[1])
            # Case 1:
            if(head[0] == tail[0] and tail[1] > head[1]+1):
                tail[1] -= 1
            # Case 2:
            elif(rad >= 4):
                if(tail[0] < head[0]):
                    tail[0] += 1
                    tail[1] -= 1
                else:
                    tail[0] -= 1
                    tail[1] -= 1

            visted.add(tuple(tail))
                
                

        
    elif(line[0] == 'D'):
        for i in range(times):
            head[0] += 1
            rad = (head[0] - tail[0]) * (head[0] - tail[0]) + (head[1] - tail[1]) * (head[1] - tail[1])
            # Case 1:
            if(head[1] == tail[1] and tail[0] < head[0]-1):
                tail[0] += 1
            # Case 2:
            elif(rad >= 4):
                if(tail[1] < head[1]):
                    tail[0] += 1
                    tail[1] += 1
                else:
                    tail[0] += 1
                    tail[1] -= 1
            visted.add(tuple(tail))
        
                
    line = f.readline()


print(len(visted))

f.close()