#hashmap version: one pass method O(n) runtime. 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i , n in enumerate(nums):
            difference = target - n
            if difference in hmap:
                return [hmap[difference], i]
            hmap[n] = i
        return

#hard code version: double for loops, O(n^2) runtime. 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
