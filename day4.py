# Program to print every line in python:

# f = open("data.txt", "r")

# line = f.readline()

# count = 0
# while line:
#     temp = line.split(',')

#     val1 = [int(i) for i in temp[0].split('-')]
#     val2 = [int(i) for i in temp[1].split('-')]
    
#     if((val1[0] <= val2[0] and val1[1] >= val2[1]) or (val1[0] >= val2[0] and val1[1] <= val2[1])):
#         count += 1

#     line = f.readline()

# f.close()

# print(count)

f = open("data.txt", "r")

line = f.readline()

count = 0
while line:
    temp = line.split(',')

    val1 = [int(i) for i in temp[0].split('-')]
    val2 = [int(i) for i in temp[1].split('-')]
    
    if(val1[1] >= val2[0] and val1[0] <= val2[0]):
        count += 1
    elif(val1[0] <= val2[1] and val1[0] >= val2[0]):
        count += 1

    line = f.readline()

f.close()

print(count)