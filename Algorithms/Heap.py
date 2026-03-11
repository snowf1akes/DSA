# Heap/Priority Queue

# Version of a queue: first in first out, but can have a priority value to pop in pop out

# min/max priority exists
# e.g. if queue = 7,3,9  and min prio = remove 3,7,9 and max is 9, 7, 3 pop

# Data Structure = Binary heap, thats (min/max)
#     - more common to use min heap
#     binary heap = complete binary tree --> every single level is going to be completly full
#                               14
#                             19   16
#                           21 26 19 68 
#     - structure property: there should be no missing nodes per level, until you add next level
#     - order property: recursive, every value in left and right subtree is less than root 
#         - !! duplicates for min heap nodes can be equal !!
#         - index 0 is skipped so binary heap maths work out.
# array eg- 0, 1, 2, 3,  4, 5, 6, 7
#         - x, 14,19,16,21,26,19, 68

#         -Left child = index * 2 (even) index
#         -right child = index * 2 + 1 (odd) index
#         -parent = index/2

# Pushing into min heap
#     - if its smaller than parent, find index i/2 and compare, then swap the values, continue recursively. 
#     code:

class Heap:
    def __init__(self):
        self.heap = [0]
    
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while self.heap[i] < self.heap[i // 2]:  #c++ method of classic swap  or can do this in python
        tmp = self.heap[i]                       #self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
        self.heap[i] = self.heap[i//2]           #i = i//2 swap index/pointer positions 
        self.heap[i//2] = tmp
        i = i // 2

#Popping min heap
#    - last node replace root, then sort downwards to maintain structure and order 

def pop(self):
    if len(self.heap) == 1:
        return None
    if len(self.heap) == 2:
        return self.heap.pop()
    
    res = self.heap[1]
    #move last value to root
    self.heap[1] = self.heap.pop()
    i = 1
    #percolate down(bubble sort downards)
    while 2 * i < len(self.heap): #checking while left node exists
        if (2 * i + 1 < len(self.heap) and self.heap[i] > self.heap[2* i + 1] and #right node exists AND swapped beginning val is > than right
            self.heap[2 * i + 1] < self.heap[2 * i]): #is Right < Left
            #swap right child
            self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i] 
            i = 2 * i + 1 #swap index pointers
        elif self.heap[i] > self.heap[2 * i ]: #curr val > left child
            #Swap left child
            self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
            i = 2 * i
        else:
            break
    return res


#Resource: Neetcode Heap properties, push and pop, heapify