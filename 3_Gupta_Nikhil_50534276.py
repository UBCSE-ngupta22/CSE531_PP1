from collections import deque

def FIFO(num, k):
    h = 0
    q = deque()
    c = 0
    for i in num:
        if len(q)!=k:
            c+=1
            if i not in q:
                q.append(i)
            else:
                h+=1
    
    for i in num[c:]:
        if i not in q:
            q.popleft()
            q.append(i)
        else:
            h+=1

    return len(num)-h

def findFarthest(a,b):
    d={}
    for i in a:
        if i in b:
            d[i]=b.index(i)
        else:
            d[i]=-1
    
    for k,v in d.items():
        if v==-1:
            return k
    return max(d, key=lambda x:d[x])

def FF(num,k):
    h= 0
    q = []
    c = 0
    for i in num:
        if len(q)!=k:
            c+=1
            if i not in q:
                q.append(i)
            else:
                h+=1

    temp = num[c:]
    for i in num[c:]:
        if i not in q:
            toReplace = findFarthest(q,temp)
            q[q.index(toReplace)] = i
            temp.remove(i)
        else:
            h+=1

    return len(num)-h

k,n,m = map(int, input().split())
num = []
while m!=0:
    num.append(int(input()))
    m-=1

print(FIFO(num,k)-FF(num,k))