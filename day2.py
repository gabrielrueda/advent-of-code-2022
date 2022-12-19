
# A/X = rock (1), B/Y = paper (2), C/Z = scissors (3) 
# 0 for loss, 3 for tie, 6 for win

# possibilites = {('X', 'A'): 4,
# ('X', 'B'): 1,
# ('X', 'C'): 7,
# ('Y', 'A'): 8,
# ('Y', 'B'): 5,
# ('Y', 'C'): 2,
# ('Z', 'A'): 3,
# ('Z', 'B'): 9,
# ('Z', 'C'): 6
# }


win = {'A': 2, 'B':3, 'C':1};

lose = {'A': 3, 'B':1, 'C':2};

tie = {'A': 1, 'B':2, 'C':3};



# Program to print every line in python:
f = open("data.txt", "r")

line = f.readline()

score = 0

while line:
    if(line[2] == 'X'):
        score += lose[line[0]]
    elif(line[2] == 'Y'):
        score += tie[line[0]] + 3
    else:
        score += win[line[0]] + 6
        
    line = f.readline()

f.close()

print(score)