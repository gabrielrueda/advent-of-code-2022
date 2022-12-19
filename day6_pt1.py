f = open("data.txt", "r")

line = f.readline()

while line:
    print(line)
    line = f.readline()

print(line)

reps = {}
i = 4

reps[line[0]] = reps.get(line[0], 0) + 1
reps[line[1]] = reps.get(line[1], 0) + 1 
reps[line[2]] = reps.get(line[2], 0) + 1
reps[line[3]] = reps.get(line[3], 0) + 1


while(len(reps) < 4):
    if(reps[line[i-4]] == 1):
        reps.pop(line[i-4])
    else:
        reps[line[i-4]] -= 1
    reps[line[i]] = reps.get(line[i], 0) + 1
    i += 1

print(f"Result is {i}")
f.close()
