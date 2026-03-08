#Move Zeroes: 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #sliding window technqiue, find non 0 as you move across array, and swap R with L indexes if R != 0, 
        #then move left along the array. 

        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1