class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen and seen[diff] != i:
                return [i, seen[diff]]
                
