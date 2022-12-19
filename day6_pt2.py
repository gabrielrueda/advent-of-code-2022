f = open("data.txt", "r")

line = f.readline()

reps = {}
i = 14

for k in range(0, 14):
    reps[line[k]] = reps.get(line[k], 0) + 1


while(len(reps) < 14):
    if(reps[line[i-14]] == 1):
        reps.pop(line[i-14])
    else:
        reps[line[i-14]] -= 1
    reps[line[i]] = reps.get(line[i], 0) + 1
    i += 1

print(f"Result is {i}")
f.close()