from heapq import heappush, heappop

def sfIntervalsPart(sfIntervals):
    
    sfIntervals.sort(key=lambda i: i[0])

    machines=[]
    heappush(machines,sfIntervals[0][1])

    for i,j in sfIntervals[1:]:
        if i >= machines[0]:
            heappop(machines)
        heappush(machines, j)

    return len(machines)

n = int(input())
sfIntervals = []
while n!=0:
    s,f = map(int, input().split())
    sfIntervals.append((s,f))
    n-=1

print(sfIntervalsPart(sfIntervals))

