#hashmap version: one pass method O(n) runtime. neetcode solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i , n in enumerate(nums):
            difference = target - n
            if difference in hmap:
                return [hmap[difference], i]
            hmap[n] = i
        return
#hashset: one pass with set[y] as difference variable: greg hogg method (faster so use in OAs)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set = {}
        #go through nums in constant time + place in hashmap
        for i in range(len(nums)):
            set[nums[i]] = i

        for i in range(len(nums)):
            #difference variable 
            y = target - nums[i]
            #make sure the other variable isn't at the same index 
            if y in set and set[y] != i:
                #return list
                return [i, set[y]]


#hard code version: double for loops, O(n^2) runtime. 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        
    
