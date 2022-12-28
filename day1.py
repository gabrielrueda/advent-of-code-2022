import heapq


f = open("data.txt", "r")

line = f.readline()

minHeap = [0,0,0]

heapq.heapify(minHeap)

curSum = 0
# maxSum = 0

while line:
    if(line == '\n'):
        if(minHeap[0] < curSum):
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, curSum)
        curSum = 0
    else:
        curSum += int(line)
    line = f.readline()

f.close()

print(sum(minHeap))