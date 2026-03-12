#longest consecutive sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for n in nums:
            #check if its the start, does it have left?
            if (n - 1) not in seen:
                length = 0
                while (n + length) in seen:
                    length += 1
                longest = max(length, longest)
        
        return longest
            