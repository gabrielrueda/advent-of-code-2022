# Program to print every line in python:
# f = open("data.txt", "r")

# line = f.readline()

# prioritySum = 0

# while line:
#     dups = set()
#     for i in range(0, int(len(line)/2)):
#         dups.add(line[i])
#     for i in range(int(len(line)/2), int(len(line))):
#         if(line[i] in dups):
#             if(line[i].isupper()):
#                 prioritySum += ord(line[i]) - 38
#             else:
#                 prioritySum += ord(line[i]) - 96
#             break
 
#     line = f.readline()

# print(prioritySum)
# f.close()


f = open("data.txt", "r")

line1 = f.readline()
line2 = f.readline()
line3 = f.readline()


prioritySum = 0

while line3:
    dups = {}
    for c in line1:
        dups[c] = 1

    for c in line2:
        if(c in dups):
            dups[c] = 2
         
    for c in line3:
        if(c in dups and dups[c] > 1):
            if(c.isupper()):
                prioritySum += ord(c) - 38
            else:
                prioritySum += ord(c) - 96
            break
 
    line1 = f.readline()
    if(not line1): break
    line2 = f.readline()
    if(not line2): break
    line3 = f.readline()

print(prioritySum)
f.close()