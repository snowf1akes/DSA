#binary search tree

from bisect import bisect_left, bisect_right, insort

#bisect_left = where a value would go in a sorted list
sorted_list = [1, 3, 5, 7, 9]

print(bisect_left(sorted_list, 5)) # 2 (index where 5 sits)
print(bisect_left(sorted_list, 6)) # 3, index spot where 6 should go
print(bisect_left(sorted_list, 0)) # 0 before everything. 
print(bisect_left(sorted_list, 10)) # 5, after everything

#insert while keeping sorted 

# !! key idea: insort = add value and keep list sorted
sorted_list = []
insort(sorted_list, 5)
print(sorted_list) # [5]
insort(sorted_list, 2)
print(sorted_list) # [2, 5]
insort(sorted_list, 8)
print(sorted_list) # [2, 5, 8]
insort(sorted_list, 5)
print(sorted_list) # [2, 5 , 5, 8]
#--> faster than sorted_list.append(x) then sorted_list.sort()

#Example practice

#obstacles at positions 3, 7, 15, 20
obstacles = []
insort(obstacles, 3)
insort(obstacles, 7)
insort(obstacles, 15)
insort(obstacles, 20)
#obstacles = [3, 7, 15, 20]
#check: any obstacle in range [5, 10]
lo , hi = 5, 10
i = bisect_left(obstacles, lo) #first obstacle >= 5
print(i) # 1 as obstacles[1] = 7 
print(i < len(obstacles) and obstacles[i] <= hi) # true, 7 is in [5, 10]

#check: any obstacle in range [8,14]?
lo, hi = 8, 14
i = bisect_left(obstacles, lo) # first obstacle >= 8
print(i) #2 as obstacles[2] = 15
print(i < len(obstacles) and obstacles[i] <= hi) #false - 15 > 14

#check: any obstacle in range[20, 25]?
lo, hi = 20, 25
i = bisect_left(obstacles, lo)
print(i < len(obstacles) and i <= hi) #true - 20 is in [20, 25]



#obsacle question simualtion

from bisect import bisect_left, insort

def solve(operations):
    obstacles = []
    result = []

    for op in operations:
        if op[0] == 1:
            #build obstacle at position x
            insort(obstacles, op[1])
        elif op[0] == 2:
            #check if block centered at x with siz can be built
            x, size = op[1], op[2]
            lo = x - (size - 1)
            hi = x + (size -1)
            i = bisect_left(obstacles, lo)
            if i < len(obstacles) and obstacles[i] <= hi:
                result.append("0")#blocked
            else:
                result.append("1") # can build
    return "".join(result)


