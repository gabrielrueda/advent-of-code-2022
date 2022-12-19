class TreeNode:
    def __init__(self, parent):
        self.dirSum = 0
        self.children = {}
        self.parent = parent

# Program to print every line in python:
f = open("data.txt", "r")

line = f.readline()
line = f.readline()

root = TreeNode(None)

curr = root

while line:
    # Change Pointer
    if(line[0:4] == "$ cd"):
        if(line[5:] == '..\n'):
            curr = curr.parent
        else:
            curr = curr.children[line[5:]]

    # new Child
    elif(line[0] == 'd'):
        curr.children[line[4:]] = TreeNode(curr)
    # Update Value
    elif(line[0] <= '9' and line[0] >= '0'):
        i = 1
        while(line[i] != ' '): i+= 1
        curr.dirSum += int(line[0:i])


    line = f.readline()

totalSum = 0
print(root.dirSum)

def dfs(visted, curRoot) -> int:
    global totalSum
    if(curRoot not in visted):
        if(len(curRoot.children) == 0):
            if(curRoot.dirSum <= 100000):
                totalSum += curRoot.dirSum
            return curRoot.dirSum
        else:
            for x in curRoot.children.values():
                curRoot.dirSum += dfs(visted, x)
            visted.add(curRoot)
            if(curRoot.dirSum <= 100000):
                totalSum += curRoot.dirSum
            return curRoot.dirSum
    return 0


visted = set()
dfs(visted, root)

print(root.dirSum)


print(totalSum)
f.close()


