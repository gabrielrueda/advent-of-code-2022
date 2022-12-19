# Program to print every line in python:
f = open("data.txt", "r")

line = f.readline()

stacks = []

for i in range(0,9):
    if(line[1+(i*4)] != " "):
        stacks.append([line[1+(i*4)]])
    else:
        stacks.append([])

line = f.readline()

while line[1] != '1':
    for i in range(0,9):
        if(line[1+(i*4)] != " "):
            # print(line[1+(i*4)])
            stacks[i].insert(0, line[1+(i*4)])
    line = f.readline()

line = f.readline()
line = f.readline()

# stacks[0].pop(0)



while line:
    # print(len(line))
    if(len(line) == 19):
        numToMove = int(line[5])
        fromA = int(line[12])-1
        toB = int(line[17])-1
        for i in range(numToMove):
            temp = stacks[fromA].pop()
            stacks[toB].append(temp)
    else:
        numToMove = int(line[5:7])
        fromA = int(line[13]) - 1
        toB = int(line[18]) - 1
        # print(f"move {numToMove} from {fromA} to {toB}")
        for i in range(numToMove):
            temp = stacks[fromA].pop()
            stacks[toB].append(temp)

    line = f.readline()

for i in range(0,9):
    print(stacks[i].pop(), end="")

print()



f.close()

