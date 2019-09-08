import heapq
import sys
import queue as Q
input = sys.stdin.readline
heap = Q.PriorityQueue()
V , E = map(int,input().split())
target = int(input())
target -= 1
dist = [ -1 ] * (V)
neighborList = [ [] for i in range(V) ]
for i in range(E):
    u, v , w = map(int,input().split())
    u -= 1
    v -= 1
    neighborList[u].append((w,v))

heap.put((0,target))

while not heap.empty() :
    pp= heap.get()
    w = pp[0]
    node = pp[1]
    if dist[node] > w or dist[node] == -1:
        dist[node] = w
        for w , linkNode in neighborList[node] :
            v = dist[node] + w
            if v < dist[linkNode] or dist[linkNode] == -1:
                heap.put((dist[node] + w,linkNode))

for i in range(0,V):
    v =dist[i]
    if v == -1 :
        print("INF")
    else :
        print(v)
