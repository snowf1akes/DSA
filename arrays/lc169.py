#Majority Element (easy)

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res, maxCount = 0, 0

        for n in nums:
            res = n if counter[n] > maxCount else res
            maxCount = max(counter[n], maxCount)
        return res
    
    