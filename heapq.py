# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:50:59 2023

@author: stud
"""
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue=[]
        self._index=0
    def enqueue(self,item,priority):
        heapq.heappush(self._queue,(priority,self._index,item))
        self._index +=1
    def dequeue(self):
        return heapq.heappop(self._queue)[-1]
    def peek(self):
        return self._queue[0][-1]
    def count(self):
        return len(self._queue)
if __name__ == "__main__":
    pq=PriorityQueue()
    pq.enqueue(1,1)
    print("Size of pq is :",pq.count(), " and peek Element is:", pq.peek())
    pq.enqueue(10,2)
    pq.enqueue(-8,3)
    print("Size of pq is :",pq.count(), " and peek Element is:", pq.peek())
    pq.dequeue()
    print("Size of pq is :",pq.count(), " and peek Element is:", pq.peek())
    pq.enqueue(25,4)
    print("Size of pq is :",pq.count(), " and peek Element is:", pq.peek())